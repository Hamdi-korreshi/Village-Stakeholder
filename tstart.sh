#!/bin/bash

# Start the Vite dev server (npm run dev) in the background
npm run dev  --prefix frontend & 
VITE_PID=$!

# Start the Django development server in the background
python backend/manage.py runserver &
DJANGO_PID=$!

echo "Vite dev server (npm run dev) running with PID $VITE_PID"
echo "Django development server running with PID $DJANGO_PID"

# Function to clean up both servers when the script is terminated
cleanup() {
    echo "Stopping Vite and Django servers..."
    kill $VITE_PID 2>/dev/null
    kill $DJANGO_PID 2>/dev/null
    exit 0
}

# Trap SIGINT (Ctrl+C) and SIGTERM signals to run the cleanup function
trap cleanup SIGINT SIGTERM

echo "Press Ctrl+C to stop both servers."

# Wait for both background processes to complete
wait