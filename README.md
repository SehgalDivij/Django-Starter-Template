# Django_Project_Template
<<<<<<< HEAD

A Django Template with Separate settings configurations for various environments to serve as boilerplate code for Other Django Projects(Not thoroughly tested yet)

### Description

Contains separate settings files for various environments:

	1. local - settings_local.py
	2. staging - settings_staging.py
	3. production - settings_production.py

Each of the above 3 files may contain separate environment specific configuration for the - local, staging and production environments.

Apart from this, the ```settings_base.py``` file contains the common parameters for the project.

Whichever settings file is active at the moment imports settings from settings_base.py and overrides the parameters that are specified in that file.

In case other environments need to be added, add another settings file in the same folder with its name preferably prefixed with ```settings_``` and ending with a term that describes the environment. E.g. If the project is being run on X's machine with specific settings, make the file name ```settings_X.py``` etc.

### How the settings file is chosen?

The appropriate settings file is chosen through the environment parameter - ```Django_Project_Template_Environment``` (replace ```Django_Project_Template``` with your project's name or some other string of your choice).

The files ```manage.py``` and ```wsgi.py``` activate the relevant settings by means of this environment variable.

To indicate a different environment, put an environment variable in the target machine/container where the project is to be run and read it in manage.py and wsgi.py files.

### Others | Coming Soon

Will add other operations such as minification later.

Will create a dockerized version of this setup that uses docker-compose later(possibly in another github repo).
=======
Boilerplate code that uses separate settings for various environments.
>>>>>>> 321ba89e29a3bec7b3cc3781f2dee372d86ba3b7
