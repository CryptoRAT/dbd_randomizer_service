import os

CSRF_TRUSTED_ORIGINS = ['https://cryptorat.com', 'https://www.cryptorat.com', 'clownfish-app-8qi77.ondigitalocean.app']
CSRF_ALLOWED_ORIGINS = ['https://cryptorat.com', 'https://www.cryptorat.com', 'clownfish-app-8qi77.ondigitalocean.app']
CORS_ORIGINS_WHITELIST = ['https://cryptorat.com', 'https://www.cryptorat.com', 'clownfish-app-8qi77.ondigitalocean.app']
ALLOWED_HOSTS = os.getenv("DJANGO_ALLOWED_HOSTS",
                          "127.0.0.1,"
                          "localhost,"
                          "clownfish-app-8qi77.ondigitalocean.app,"
                          "https://www.cryptorat.com,"
                          "https://cryptorat.com").split(",")
DEBUG = True