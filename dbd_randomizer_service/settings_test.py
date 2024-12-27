import os
SECRET_KEY = "test has some of the secrets"
DEBUG = False
ALLOWED_HOSTS = ['localhost']
DATABASE_NAME = "dbd_randomizer_db_test"
DATABASE_USER = "test_user"
DATABASE_PASSWORD = "test_password"
DATABASE_HOST = "localhost"
DATABASE_PORT = 5432
CSRF_COOKIE_SAMESITE = 'None'
CSRF_COOKIE_SECURE = False
CSRF_COOKIE_DOMAIN = 'localhost'
CSRF_TRUSTED_ORIGINS = ['http://localhost:3000', 'https://localhost:3000']
CSRF_ALLOWED_ORIGINS = ['http://localhost:3000', 'https://localhost:3000']
CORS_ORIGINS_WHITELIST = ['http://localhost:3000', 'https://localhost:3000']