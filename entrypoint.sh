#!/bin/bash
set -e

echo "Waiting for PostgreSQL at db:5432..."
# Using Bash's /dev/tcp to check connection
while ! (echo > /dev/tcp/db/5432) 2>/dev/null; do
  sleep 1
done

echo "PostgreSQL is up. Starting Django..."
exec "$@"