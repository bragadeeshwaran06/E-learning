import os
from .base import *

DEBUG = True

DATABASES['default'].update({
    'NAME': 'educa',  
    'USER': 'testpress',  
    'PASSWORD': 'testpress1$', 
})
