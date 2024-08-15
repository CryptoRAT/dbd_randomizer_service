#!/bin/bash
echo "Environment: $DJANGO_ENV"

echo "Allowed hosts: $ALLOWED_HOSTS"

# Apply database migrations
echo "Applying database migrations..."
python manage.py migrate

echo "Starting server..."
python manage.py runserver 0.0.0.0:8000