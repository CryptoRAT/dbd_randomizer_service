import os

DEBUG = False
DATABASE_NAME = os.getenv("DATABASE_NAME")
DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD")
DATABASE_HOST = os.getenv("DATABASE_HOST")
DATABASE_USER = os.getenv("DATABASE_USER")
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