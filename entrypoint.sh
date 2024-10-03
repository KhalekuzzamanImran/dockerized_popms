#!/bin/sh

# Exit immediately if a command exits with a non-zero status
set -e

# Navigate to the app directory
cd /opt/popms_backend

# Collect static files
echo "=========================================Collecting static files========================================="
python manage.py collectstatic --noinput

# Apply database migrations
echo "=========================================Applying database migrations========================================"
python manage.py migrate --noinput

# Start the Gunicorn server
echo "=========================================Starting Gunicorn========================================="
gunicorn --chdir=/opt/app \
    --workers=4 \
    --threads=6 \
    --worker-class=gthread \
    --preload \
    --bind :5000 \
    --log-level=info \
    --error-logfile - \
    --access-logfile - \
    --capture-output \
    popms.wsgi:application

# Navigate back to the previous directory (optional)
cd -
