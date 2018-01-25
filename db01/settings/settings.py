"""
Django settings for db01 project.

Generated by 'django-admin startproject' using Django 1.11.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""


try:
    from settings_base import *
except ImportError as e:
    pass


try:
    from settings_dev import *
except ImportError as e:
    pass

try:
    from settings_prod import *
except ImportError as e:
    pass


