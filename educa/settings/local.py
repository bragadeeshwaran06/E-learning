import os
from .base import *

DEBUG = True

DATABASES = {
    'default': {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
 }
}
#psql -U testpress -h localhost -p 5432 educa