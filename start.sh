#!/bin/bash
echo "Environment..."
echo $DJANGO_ENV
echo "Allowed hosts..."
echo $ALLOWED_HOSTS
# Apply database migrations
echo "Applying database migrations..."
python manage.py migrate

echo "Starting server..."
python manage.py runserver 0.0.0.0:8000