from .base import *

DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.mysql',
    'NAME': 'my_db',
    'USER': 'dev',
    'PASSWORD': 'root',
    'HOST': 'localhost',
    'PORT': '3307',
    'OPTIONS': {
      'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
    },
  }
}