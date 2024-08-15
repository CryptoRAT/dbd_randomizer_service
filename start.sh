#!/bin/bash
ENVIRONMENT = os.environ.get('DJANGO_ENV', 'development')
HOSTS_ALLOWED = os.environ.get('ALLOWED_HOSTS')
echo "Environment..."
echo $ENVIRONMENT
echo "Allowed hosts..."
echo $HOSTS_ALLOWED
# Apply database migrations
echo "Applying database migrations..."
python manage.py migrate

echo "Starting server..."
python manage.py runserver 0.0.0.0:8000