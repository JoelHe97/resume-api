from .base import *

ALLOWED_HOSTS = ["*"]

DEBUG = True

DATABASES = {
    "default": {
        "ENGINE": os.environ.get("DB_PROD_ENGINE"),
        "NAME": os.environ.get("DB_PROD_NAME"),
        "HOST": os.environ.get("DB_PROD_HOST"),
        "PORT": os.environ.get("DB_PROD_PORT"),
        "Trusted_Connection": "no",
        "OPTIONS": {
            "driver": "ODBC Driver 17 for SQL Server",
            "extra_params": os.environ.get("DB_EXTRA_PARAMS"),
        },
    }
}

INSTALLED_APPS += ["debug_toolbar"]


INTERNAL_IPS = [
    "127.0.0.1",
]
