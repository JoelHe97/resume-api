import os


def get_sas(filename):
    from azure.storage.blob import BlobServiceClient

    blob_service_client = BlobServiceClient.from_connection_string(
        "DefaultEndpointsProtocol=https;AccountName=resumebucket;AccountKey=61QyF+BPJXmiDKjP1IFAn8bCJSjcm5ndSnq9py9QMXX7HeoDo2KyLKd5Own2P/0ES5+iVWwI44DN+AStdHGFww==;EndpointSuffix=core.windows.net"
    )

    from datetime import datetime, timedelta
    from azure.storage.blob import (
        ResourceTypes,
        AccountSasPermissions,
        generate_account_sas,
    )

    sas_token = generate_account_sas(
        blob_service_client.account_name,
        account_key=blob_service_client.credential.account_key,
        resource_types=ResourceTypes(object=True),
        permission=AccountSasPermissions(read=True),
        expiry=datetime.utcnow() + timedelta(minutes=1),
    )

    sas_url = (
        "https://"
        + os.environ.get("AZURE_ACCOUNT_NAME")
        + ".blob.core.windows.net/"
        + os.environ.get("AZURE_CONTAINER")
        + "/"
        + filename
        + "?"
        + sas_token
    )
    return sas_url
