"""Logging Configuration."""
# I usually store logs in the /home/user/logs/<app_name> directory
# parent_log_dir = '../../logs/<app_name>'
parent_log_dir = '../../logs/DjangoProjectTemplate'

dev_log = '{}/dev'.format(parent_log_dir)
prod_log = '{}/prod'.format(parent_log_dir)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'loggers': {
        'django': {
            'handlers': ['console'],
        },
        'py.warnings': {
            'handlers': ['console', 'prod', 'dev'],
        },
        'django.request': {
            'handlers': ['console', 'prod', 'dev'],
            'level': 'DEBUG',
            'propagate': False
        },
        'django.server': {
            'handlers': ['null']
        }
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
        'null': {
            'class': 'logging.NullHandler',
        },
        'dev': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.FileHandler',
            'formatter': 'simple',
            'filename': dev_log
        },
        # For ease of use, staging and production will log to the same handler.
        'prod': {
            'level': 'WARNING',
            'filters': ['require_debug_false'],
            'class': 'logging.FileHandler',
            'formatter': 'verbose',
            'filename': prod_log
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'formatters': {
        'simple': {
            'format': '[%(asctime)s] %(levelname)s %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S'
        },
        'verbose': {
            'format': '[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S'
        }
    }
}
