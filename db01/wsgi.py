"""
WSGI config for db01 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os

# ---------------->>>>>>>>>>>>>>>
import django
# <<<<<<<<<<<<<<<<<<-------------

#from django.core.wsgi import get_wsgi_application ##### First option

#import sys

#path='/home/robert/Documents/GBeka-Project/gbenv01/db01/db01'

#if path not in sys.path:
#	sys.path.append(path)


#os.environ.setdefault("DJANGO_SETTINGS_MODULE", "db01.settings")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "db01.settings.settings")

# ---------------->>>>>>>>>>>>>>>
django.setup()
from django.contrib.auth.handlers.modwsgi import check_password, groups_for_user
from django.core.handlers.wsgi import WSGIHandler
application = WSGIHandler()
# <<<<<<<<<<<<<<<<<<-------------

#application = get_wsgi_application()	##### First option



#import django.core.handlers.wsgi
#application = django.core.handlers.wsgi.WSGIHandler()
