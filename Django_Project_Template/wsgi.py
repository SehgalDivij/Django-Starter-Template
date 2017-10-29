import os

from django.core.wsgi import get_wsgi_application
modules = {
    'LOCAL': 'Django_Project_Template.settings_local',
    'STAGING': 'Django_Project_Template.settings_staging',
    'PRODUCTION': 'Django_Project_Template.settings_production'
}
current_env = os.environ.get('Django_Project_Template_Environment', "LOCAL")
settings_module = modules[current_env]
os.environ.setdefault("DJANGO_SETTINGS_MODULE",
                      settings_module)


application = get_wsgi_application()
