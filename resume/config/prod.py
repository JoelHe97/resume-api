from .base import *

ALLOWED_HOSTS = ["*"]

DEBUG = False
DATABASES = {
    "default": {
        "ENGINE": os.environ.get("DB_PROD_ENGINE"),
        "NAME": os.environ.get("DB_PROD_NAME"),
        "USER": os.environ.get("DB_PROD_USER"),
        "PASSWORD": os.environ.get("DB_PROD_PASSWORD"),
        "HOST": os.environ.get("DB_PROD_HOST"),
        "PORT": os.environ.get("DB_PROD_PORT"),
    }
}
