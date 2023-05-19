from .base import *


def get_CSRF_TRUSTED_ORIGINS():
    CSRF_TRUSTED_ORIGINS_FROM_ENVIRON = os.environ.get("ALLOWED_HOSTNAME")
    return [s.strip() for s in CSRF_TRUSTED_ORIGINS_FROM_ENVIRON.split(",")]


ALLOWED_HOSTS = get_CSRF_TRUSTED_ORIGINS()

print(ALLOWED_HOSTS)
DEBUG = False
DATABASES = {
    "default": {
        "ENGINE": os.environ.get("DB_PROD_ENGINE"),
        "NAME": os.environ.get("DB_PROD_NAME"),
        "HOST": os.environ.get("DB_PROD_HOST"),
        "PORT": os.environ.get("DB_PROD_PORT"),
        "Trusted_Connection": "no",
        "OPTIONS": {
            "driver": "ODBC Driver 17 for SQL Server",
            "extra_params": "Driver={ODBC Driver 17 for SQL Server};Server=tcp:joelhe.database.windows.net,1433;Database=resume-api;Uid={2016014076@unfv.edu.pe};Pwd={Huacre0123};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;Authentication=ActiveDirectoryPassword",
        },
    }
}
