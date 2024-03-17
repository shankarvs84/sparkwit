import os
import time
import traceback

from azure.storage.blob import BlobServiceClient
from dotenv import load_dotenv


def load_blob():
    try:
        load_dotenv()
        connection_string = os.environ.get("AZURE_CONN_STRING")
        container_name = os.environ.get("CONTAINER_NAME")  # name of the container created within Azure storage account
        blob_service_client = BlobServiceClient.from_connection_string(connection_string)

        directory_path = "Data"

        for root, dirs, files in os.walk(directory_path):
            for file in files:
                file_path = os.path.join(root, file)

                blob_name = os.path.relpath(file_path, directory_path)
                with open(file_path, "rb") as data:
                    blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)
                    blob_client.upload_blob(data, overwrite=True)
                    print(f'Data from {file_path} loaded in blob storage named {blob_name}')
                    time.sleep(5)
        return True
    except Exception as e:
        tb = traceback.format_exc()
        print(e, tb)
        return False
