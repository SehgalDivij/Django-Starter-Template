from .settings_base import *

ALLOWED_HOSTS = ['*', 'web']

DEBUG = True

# Change these settings for your setup.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Add other local settings here.