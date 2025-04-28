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

CACHES = {
  "default": {
    "BACKEND": "django_redis.cache.RedisCache",
    "LOCATION": "redis://127.0.0.1:6379/1",
    "OPTIONS": {
      "CLIENT_CLASS": "django_redis.client.DefaultClient",
    }
  }
}
