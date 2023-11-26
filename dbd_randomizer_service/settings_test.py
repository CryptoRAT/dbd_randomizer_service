from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
# This should be kept in sync with main settings.py. If you change one, change the other.
# TODO: Better yet find a way to combine them so we only need to update one place.
BASE_DIR = Path(__file__).resolve().parent.parent

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    },
}