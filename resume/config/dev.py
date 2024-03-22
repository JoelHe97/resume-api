from .base import *

ALLOWED_HOSTS = ["*"]

DEBUG = True

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": os.environ.get("DB_PROD_NAME"),
        "HOST": os.environ.get("DB_PROD_HOST"),
        "USER": os.environ.get("DB_PROD_USER"),
        "PASSWORD": os.environ.get("DB_PROD_PASSWORD"),
        "PORT": os.environ.get("DB_PROD_PORT"),
    }
}

INSTALLED_APPS += ["debug_toolbar"]


INTERNAL_IPS = [
    "127.0.0.1",
]
