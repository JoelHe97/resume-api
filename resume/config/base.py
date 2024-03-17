"""
Django settings for app project.

Generated by 'django-admin startproject' using Django 4.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

import os
from pathlib import Path

from dotenv import load_dotenv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv()


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY")

# Application definition
DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]
LOCAL_APPS = [
    "apps.users",
    "apps.locations",
    "apps.skills",
    "apps.careers",
    "apps.languages",
    "apps.projects",
]

THIRD_APPS = [
    "rest_framework",
    "corsheaders",
    "ckeditor",
    "storages",
]

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://redis-18578.c281.us-east-1-2.ec2.cloud.redislabs.com:18578",
        "TIMEOUT": None,
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "PASSWORD": "NlbHNoUK6yNkJ0LJjy72WIjlWS69qG9H",
        },
    }
}
print(CACHES["default"])
REST_FRAMEWORK_EXTENSIONS = {
    "DEFAULT_CACHE_KEY_FUNC": "rest_framework_extensions.utils.default_cache_key_func"
}


def get_CORS_ALLOWED_ORIGIN():
    CORS_ALLOWED_ORIGIN_FROM_ENVIRON = os.environ.get("CORS_ALLOWED_ORIGIN")
    return [s.strip() for s in CORS_ALLOWED_ORIGIN_FROM_ENVIRON.split(",")]


def get_CORS_ORIGIN_WHITELIST():
    CORS_ORIGIN_WHITELIST_FROM_ENVIRON = os.environ.get("CORS_ORIGIN_WHITELISTS")
    return [s.strip() for s in CORS_ORIGIN_WHITELIST_FROM_ENVIRON.split(",")]


def get_CSRF_TRUSTED_ORIGINS():
    CSRF_TRUSTED_ORIGINS_FROM_ENVIRON = os.environ.get("CSRF_TRUSTED_ORIGINS")
    return [s.strip() for s in CSRF_TRUSTED_ORIGINS_FROM_ENVIRON.split(",")]


CORS_ALLOWED_ORIGINS = get_CORS_ALLOWED_ORIGIN()
CORS_ORIGIN_WHITELIST = get_CORS_ORIGIN_WHITELIST()
CSRF_TRUSTED_ORIGINS = get_CSRF_TRUSTED_ORIGINS()


INSTALLED_APPS = DJANGO_APPS + LOCAL_APPS + THIRD_APPS

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "resume.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "resume.wsgi.application"

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

CKEDITOR_CONFIGS = {
    "default": {
        "toolbar": "full",
        "height": 300,
        "width": 800,
    },
}
# AWS_QUERYSTRING_AUTH = False
X_FRAME_OPTIONS = "SAMEORIGIN"

REST_FRAMEWORK = {
    "DEFAULT_RENDERER_CLASSES": [
        "rest_framework.renderers.JSONRenderer",
        "rest_framework.renderers.BrowsableAPIRenderer",
    ],
    "DEFAULT_CHARSET": "utf-8",
}
# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)


MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")


# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

AUTH_USER_MODEL = "users.User"


EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_USE_TLS = True  # O False si no se requiere cifrado TLS
EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD")
EMAIL_USE_TLS = True


# DEFAULT_FILE_STORAGE = "storages.backends.azure_storage.AzureStorage"
# STATICFILES_STORAGE = "resume.storages.custom_azure.PublicAzureStorage"

# django >= 4.2
DEFAULT_FILE_STORAGE = os.environ.get("DEFAULT_FILE_STORAGE")
STATICFILES_STORAGE = os.environ.get("STATICFILES_STORAGE")

AZURE_CONTAINER = os.environ.get("AZURE_CONTAINER")
AZURE_ACCOUNT_KEY = os.environ.get("AZURE_ACCOUNT_KEY")
AZURE_ACCOUNT_NAME = os.environ.get("AZURE_ACCOUNT_NAME")
# AZURE_CUSTOM_DOMAIN = f'{"resumebucket2"}.blob.core.windows.net'
AWS_S3_ACCESS_KEY_ID = os.environ.get("AWS_S3_ACCESS_KEY_ID")
AWS_S3_SECRET_ACCESS_KEY = os.environ.get("AWS_S3_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = os.environ.get("AWS_STORAGE_BUCKET_NAME")

CKEDITOR_BASEPATH = os.environ.get("CKEDITOR_BASEPATH")
AWS_DEFAULT_ACL = "public-read"
AWS_S3_CUSTOM_DOMAIN = f"{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com"
AWS_S3_OBJECT_PARAMETERS = {"CacheControl": "max-age=86400"}
# s3 static settings
AWS_LOCATION = "static"
STATIC_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/static/"
