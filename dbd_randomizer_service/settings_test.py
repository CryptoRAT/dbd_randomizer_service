from pathlib import Path
import os
from .settings import *

CSRF_COOKIE_SAMESITE = 'None'
CSRF_COOKIE_SECURE = False
CORS_ALLOW_CREDENTIALS = True
RUN_SERVER_SSL = "/Users/lukelliot/certs/cert.crt"
RUN_SERVER_SSL_KEY = "/Users/lukelliot/certs/key.key"
DEBUG = True

CSRF_COOKIE_DOMAIN = 'localhost'
CSRF_TRUSTED_ORIGINS = ['http://localhost:3000', 'https://localhost:3000']
CSRF_ALLOWED_ORIGINS = ['http://localhost:3000', 'https://localhost:3000']
CORS_ORIGINS_WHITELIST = ['http://localhost:3000', 'https://localhost:3000']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    },
}