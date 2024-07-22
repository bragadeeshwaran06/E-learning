from .base import *

DEBUG = False

ADMINS = (
 ('testpress', 'bragadeeshwaran@testpress.in'),
)

ALLOWED_HOSTS = ['*']

DATABASES = {
 'default': {
    'ENGINE': 'django.db.backends.postgresql',
    'NAME': 'educa',
    'USER': 'educa',
    'PASSWORD': '*****',
 }
}