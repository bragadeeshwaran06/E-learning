from .base import *

DEBUG = False

ADMINS = (
 ('testpress', 'bragadeeshwaran@testpress.in'),
)

ALLOWED_HOSTS = ['.educaproject.com']

DATABASES['default'].update({
    'NAME': 'educa',  
    'USER': 'testpress',  # Replace with your production database username
    'PASSWORD': 'testpress1$',  # Replace with your production database password
    'HOST': 'localhost',  # Replace with your production database host
    'PORT': '5432',  # Replace with your production database port
})

SECURE_SSL_REDIRECT = True
CSRF_COOKIE_SECURE = True