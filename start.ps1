# Check for required commands
if (-not (Get-Command python -ErrorAction SilentlyContinue)) { Write-Host "Error: Python is not installed."; exit }
if (-not (Get-Command npm -ErrorAction SilentlyContinue)) { Write-Host "Error: npm is not installed."; exit }
if (-not (Get-Command psql -ErrorAction SilentlyContinue)) { Write-Host "Warning: PostgreSQL (psql) not found. Ensure PostgreSQL is installed and running." }

# Create virtual environment if missing (in backend\env)
if (-not (Test-Path ".\backend\env")) {
    Write-Host "Creating virtual environment in backend\env"
    python -m venv .\backend\env
    if ($LASTEXITCODE -ne 0) { Write-Host "Failed to create virtual environment."; exit }
}

# Activate virtual environment and install backend dependencies
.\backend\env\Scripts\Activate.ps1
pip install -r .\backend\requirements.txt

# Run Django migrations
python .\backend\manage.py migrate

# Start Django server in a new process (background)
Start-Process -FilePath python -ArgumentList ".\backend\manage.py runserver 0.0.0.0:8000"

# Change to frontend, install dependencies, and start Vue (Vite) dev server
Set-Location -Path .\frontend
npm install
npm run dev -- --host
