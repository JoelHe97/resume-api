from .base import *

ALLOWED_HOSTS = ["*"]

DEBUG = True

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "resume",
        "USER": "root",
        "PASSWORD": "",
        "HOST": "localhost",
        "PORT": 3306,
    }
}

INSTALLED_APPS += ["debug_toolbar"]


INTERNAL_IPS = [
    "127.0.0.1",
]
