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
        "PORT": os.environ.get("DB_PROD_PORT"),
        "Trusted_Connection": "no",
        "OPTIONS": {
            "driver": "ODBC Driver 17 for SQL Server",
            "extra_params": "Driver={ODBC Driver 17 for SQL Server};Server=tcp:joelhe.database.windows.net,1433;Database=resume-api;Uid={2016014076@unfv.edu.pe};Pwd={Huacre0123};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;Authentication=ActiveDirectoryPassword",
        },
    }
}
