from storages.backends.azure_storage import AzureStorage
from dotenv import load_dotenv
import os

load_dotenv()


class StaticStorage(AzureStorage):
    account_name = os.environ.get("AZURE_ACCOUNT_NAME")
    account_key = os.environ.get("AZURE_ACCOUNT_KEY")
    azure_container = os.environ.get("AZURE_CONTAINER_STATIC")
    expiration_secs = None
