from .settings_base import *

ALLOWED_HOSTS = ['*', 'web']

# You should change this.
DEBUG = False

# Change these settings for your setup.
DATABASES = {
    'default': {
        'ENGINE': 'DB_BACKEND_ENGINE',
        'HOST': 'HOST_RUNNING_DB',
        'PORT': '3306',
        'NAME': 'DB_NAME',
        'USER': 'DB_USER_NAME',
        'PASSWORD': 'DB_USER_PASSWORD'
    }
}

# Add production specific settings here.
