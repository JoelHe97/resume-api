from .base import *


ALLOWED_HOSTS = (
    [os.environ["WEBSITE_HOSTNAME"]] if "WEBSITE_HOSTNAME" in os.environ else []
)

DEBUG = False
DATABASES = {
    "default": {
        "ENGINE": os.environ.get("DB_PROD_ENGINE"),
        "NAME": os.environ.get("DB_PROD_NAME"),
        "HOST": os.environ.get("DB_PROD_HOST"),
        "USER": os.environ.get("DB_PROD_USER"),
        "PASSWORD": os.environ.get("DB_PROD_PASSWORD"),
        "PORT": os.environ.get("DB_PROD_PORT"),
    }
}
