from .base import *
from decouple import config
ALLOWED_HOSTS = ['*']

DEBUG = False
DATABASES = {
    'default': {
        'ENGINE': config('DB_PROD_ENGINE'),
        'NAME': config('DB_PROD_NAME'),
        'USER': config('DB_PROD_USER'),
        'PASSWORD': config('DB_PROD_PASSWORD'),
        'HOST': config('DB_PROD_HOST'),
        'PORT': config('DB_PROD_PORT'),
    }
}
