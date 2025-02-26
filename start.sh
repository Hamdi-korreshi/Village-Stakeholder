#!/bin/bash
# Check for required commands
command -v python >/dev/null 2>&1 || { echo "Error: Python is not installed."; exit 1; }
command -v npm >/dev/null 2>&1 || { echo "Error: npm is not installed."; exit 1; }
command -v psql >/dev/null 2>&1 || echo "Warning: PostgreSQL (psql) not found. Please ensure PostgreSQL is installed and running."

# Create virtual environment if missing (in backend/env)
[ -d "backend/env" ] || { echo "Creating virtual environment in backend/env"; python -m venv backend/env || { echo "Failed to create virtual environment."; exit 1; } }

# Activate virtual environment and install backend dependencies
source backend/env/bin/activate
pip install -r backend/requirements.txt

# Run Django migrations and start the Django server in the background
python backend/manage.py migrate
python backend/manage.py runserver 0.0.0.0:8000 &

# Change to frontend directory, install dependencies, and start Vue (Vite) dev server
cd frontend || { echo "Error: Cannot change to frontend directory."; exit 1; }
npm install
npm run dev -- --host
