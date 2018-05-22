from .base import *

DEBUG = False

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases
with open('/secrets/ImOkCore.password', 'r') as secret:
    db_password = secret.read().strip()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'im-ok-core-db',
        'USER': 'im-ok-core',
        'PASSWORD': db_password,
        'HOST': 'tbd',
        'PORT': '5432',
        'CONN_MAX_AGE': 30
    }
}

