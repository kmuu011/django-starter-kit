from .base import *

DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.mysql',
    'NAME': 'my_db',
    'USER': 'prod',
    'PASSWORD': 'root',
    'HOST': '172.28.0.4',
    'PORT': '3307',
    'OPTIONS': {
      'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
    },
  }
}