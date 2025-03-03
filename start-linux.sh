#!/usr/bin/env bash
set -euo pipefail

# Load .env if available
[ -f .env ] && export $(grep -v '^#' .env | xargs)

# Check required commands
command -v python >/dev/null 2>&1 || { echo "Error: Python is not installed."; exit 1; }
command -v npm >/dev/null 2>&1 || { echo "Error: npm is not installed."; exit 1; }

# Install PostgreSQL if psql not found
if ! command -v psql >/dev/null 2>&1; then
  echo "PostgreSQL (psql) not found. Installing via apt-get..."
  sudo apt-get update && sudo apt-get install -y postgresql postgresql-contrib postgresql-common
fi

# Start PostgreSQL cluster if not running
if command -v pg_lsclusters >/dev/null 2>&1; then
  cluster_line=$(pg_lsclusters | awk 'NR==2')
  if [ -z "$cluster_line" ]; then
    echo "No PostgreSQL cluster found. Initializing a new cluster..."
    sudo pg_createcluster 14 main --start
  else
    cluster_status=$(echo "$cluster_line" | awk '{print $4}')
    if [ "$cluster_status" != "online" ]; then
      version=$(echo "$cluster_line" | awk '{print $1}')
      cluster=$(echo "$cluster_line" | awk '{print $2}')
      echo "Starting PostgreSQL cluster $version $cluster..."
      sudo pg_ctlcluster "$version" "$cluster" start
    fi
  fi
else
  if systemctl is-active --quiet postgresql; then
    echo "PostgreSQL service is active."
  else
    echo "Starting PostgreSQL service via systemctl..."
    sudo systemctl start postgresql
  fi
fi

# Wait a few seconds for the server to start
sleep 2

# Test connection via TCP
if ! psql -h localhost -U postgres -c "SELECT 1;" >/dev/null 2>&1; then
  echo "Error: Unable to connect to PostgreSQL on localhost. Please check listen_addresses and pg_hba.conf."
  exit 1
fi

# Set PGPASSWORD if DB_POSTGRES_PASSWORD is provided
if [ -n "${DB_POSTGRES_PASSWORD:-}" ]; then
  export PGPASSWORD="${DB_POSTGRES_PASSWORD}"
fi

# Use postgres user if available, otherwise fallback
if getent passwd postgres >/dev/null; then
  PSQL_CMD="sudo -u postgres psql -h localhost"
else
  PSQL_CMD="psql -h localhost"
fi

# Create app database and user if variables are provided
if [ -n "${DB_NAME:-}" ] && [ -n "${DB_USER:-}" ] && [ -n "${DB_PASSWORD:-}" ]; then
  $PSQL_CMD -tc "SELECT 1 FROM pg_roles WHERE rolname = '$DB_USER'" | grep -q 1 || $PSQL_CMD -c "CREATE USER $DB_USER WITH PASSWORD '$DB_PASSWORD';"
  $PSQL_CMD -lqt | cut -d \| -f 1 | grep -qw "$DB_NAME" || $PSQL_CMD -c "CREATE DATABASE $DB_NAME OWNER $DB_USER;"
fi

# Set up Python virtual environment for backend
[ -d "backend/env" ] || { echo "Creating virtual environment in backend/env"; python -m venv backend/env; }
source backend/env/bin/activate
pip install -r backend/requirements.txt

# Run Django migrations and server in background
python backend/manage.py migrate
python backend/manage.py runserver 0.0.0.0:8000 &

# Set up and run Vite dev server for frontend
cd frontend || { echo "Error: Cannot change to frontend directory."; exit 1; }
npm install
npm run dev -- --host

# When Vite stops, kill Django server
kill %1
