# Import the Secret Manager client library.
from google.cloud import secretmanager
from google.oauth2.service_account import Credentials


def access_secret_version(secret_id, version_id="latest"):
    # Create the Secret Manager client.
    client = secretmanager.SecretManagerServiceClient()

    # Build the resource name of the secret version.
    name = f"projects/772712225952/secrets/{secret_id}/versions/{version_id}"
    # Access the secret version.
    response = client.access_secret_version(name=name)

    # Return the decoded payload.
    return response.payload.data.decode('UTF-8')
    
import json


def get_credentials_from_token(secret_payload:str)->Credentials:
    """Given an authentication token, return a Credentials object"""
    
    credential_dict = json.loads(secret_payload)
    return Credentials.from_service_account_info(credential_dict)