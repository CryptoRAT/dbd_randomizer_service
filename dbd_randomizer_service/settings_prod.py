DEBUG = False
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