# 参考ページ
# https://learn.microsoft.com/ja-jp/azure/storage/blobs/storage-quickstart-blobs-python?tabs=managed-identity%2Croles-azure-portal%2Csign-in-azure-cli&pivots=blob-storage-quickstart-scratch

import os
import uuid
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient


def get_blob_service_client_account_key():
    # TODO: Replace <storage-account-name> with your actual storage account name
    account_url = "https://<storage-account-name>.blob.core.windows.net"
    shared_access_key = os.getenv("AZURE_STORAGE_ACCESS_KEY")
    credential = shared_access_key

    # Create the BlobServiceClient object
    blob_service_client = BlobServiceClient(account_url, credential=credential)

    return blob_service_client


# 予め環境変数 AZURE_STORAGE_CONNECTION_STRING に接続文字列を設定しておく
# Linuxの場合
# export AZURE_STORAGE_CONNECTION_STRING=""
# 接続文字列は、ストレージアカウント＞アクセスキー で取得する
def get_blob_service_client_connection_string():
    # TODO: Replace <storage-account-name> with your actual storage account name
    account_url = "https://<storage-account-name>.blob.core.windows.net"
    connection_string = os.getenv("AZURE_STORAGE_CONNECTION_STRING")

    # Create the BlobServiceClient object
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)

    return blob_service_client

# 接続文字列から、BlobServiceClient object を生成
blob_service_client = get_blob_service_client_connection_string()

# コンテナ名
container_name = "imageanalysis"

# Create a local directory to hold blob data
local_path = "./data"
if not os.path.exists(local_path):
    os.mkdir(local_path)

try:
    # Create a file in the local data directory to upload and download
    local_file_name = str(uuid.uuid4()) + ".txt"
    upload_file_path = os.path.join(local_path, local_file_name)

    # Write text to the file
    file = open(file=upload_file_path, mode='w')
    file.write("Hello, World!")
    file.close()

    # Create a blob client using the local file name as the name for the blob
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=local_file_name)

    print("\nUploading to Azure Storage as blob:\n\t" + local_file_name)

    # Upload the created file
    with open(file=upload_file_path, mode="rb") as data:
        blob_client.upload_blob(data)

except Exception as e:
    # その他の例外が発生した場合の処理
    print(f"予期しないエラーが発生しました: {e}")

finally:
    # 必ず実行される処理
    print("処理が完了しました")

print("\nListing blobs...")


# List the blobs in the container
container_client = blob_service_client.get_container_client(container=container_name) 
blob_list = container_client.list_blobs()
for blob in blob_list:
    print("\t" + blob.name, blob.last_modified)

# Download the blob to a local file
# Add 'DOWNLOAD' before the .txt extension so you can see both files in the data directory
download_file_path = os.path.join(local_path, str.replace(local_file_name ,'.txt', 'DOWNLOAD.txt'))
container_client = blob_service_client.get_container_client(container=container_name) 
print("\nDownloading blob to \n\t" + download_file_path)

with open(file=download_file_path, mode="wb") as download_file:
    download_file.write(container_client.download_blob(blob.name).readall())
