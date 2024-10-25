#!/bin/bash
# Apply database migrations
echo "Applying database migrations..."
python manage.py migrate

echo "Starting Gunicorn..."
gunicorn dbd_randomizer_service.wsgi:application --bind 0.0.0.0:8000 --workers 3
