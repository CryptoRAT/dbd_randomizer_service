import os
from django.core.management.utils import get_random_secret_key

DEBUG = False
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", get_random_secret_key())
DATABASE_NAME = os.getenv("DATABASE_NAME")
DATABASE_USER = os.getenv("DATABASE_USER")
DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD")
DATABASE_HOST = os.getenv("DATABASE_HOST")
DATABASE_PORT = os.getenv("DATABASE_PORT")
ALLOWED_HOSTS = [
    "127.0.0.1",
    "localhost",
    "https://services.lupogreybeard.com",
    "http://services.lupogreybeard.com",
    "services.lupogreybeard.com",
    "https://www.lupogreybeard.com",
    "https://lupogreybeard.com",
]
CSRF_TRUSTED_ORIGINS = [
    'https://lupogreybeard.com',
    'https://www.lupogreybeard.com',
    'http://clownfish-app-8qi77.ondigitalocean.app',
    'https://clownfish-app-8qi77.ondigitalocean.app'
]
CSRF_ALLOWED_ORIGINS = [
    'https://lupogreybeard.com',
    'https://www.lupogreybeard.com',
    'http://clownfish-app-8qi77.ondigitalocean.app',
    'https://clownfish-app-8qi77.ondigitalocean.app'
]
CORS_ORIGINS_WHITELIST = [
    'https://lupogreybeard.com',
    'https://www.lupogreybeard.com',
    'http://clownfish-app-8qi77.ondigitalocean.app',
    'https://clownfish-app-8qi77.ondigitalocean.app'
]