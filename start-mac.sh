#!/usr/bin/env bash
set -euo pipefail

[ -f .env ] && export $(grep -v '^#' .env | xargs)

command -v python >/dev/null 2>&1 || { echo "Error: Python is not installed."; exit 1; }
command -v npm >/dev/null 2>&1 || { echo "Error: npm is not installed."; exit 1; }

if ! command -v psql >/dev/null 2>&1; then
  echo "PostgreSQL (psql) not found. Installing via Homebrew..."
  brew update && brew install postgresql
fi

if [ -n "${DB_NAME:-}" ] && [ -n "${DB_USER:-}" ] && [ -n "${DB_PASSWORD:-}" ]; then
  psql -tc "SELECT 1 FROM pg_roles WHERE rolname = '$DB_USER'" | grep -q 1 || psql -c "CREATE USER $DB_USER WITH PASSWORD '$DB_PASSWORD';"
  psql -lqt | cut -d \| -f 1 | grep -qw "$DB_NAME" || psql -c "CREATE DATABASE $DB_NAME OWNER $DB_USER;"
fi

[ -d "backend/env" ] || { echo "Creating virtual environment in backend/env"; python -m venv backend/env || { echo "Failed to create virtual environment."; exit 1; } }
source backend/env/bin/activate
pip install -r backend/requirements.txt

python backend/manage.py migrate
python backend/manage.py runserver 0.0.0.0:8000 &

cd frontend || { echo "Error: Cannot change to frontend directory."; exit 1; }
npm install
npm run dev -- --host

kill %1
