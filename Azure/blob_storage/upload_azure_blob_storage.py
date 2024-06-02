# Azure Blob Storage に対してファイルをアップロード／ダウンロードする
# 参考ページ
# https://learn.microsoft.com/ja-jp/azure/storage/blobs/storage-quickstart-blobs-python?tabs=managed-identity%2Croles-azure-portal%2Csign-in-azure-cli&pivots=blob-storage-quickstart-scratch

import os
import uuid
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

# 初期設定
# TODO: Replace <storage-account-name> with your actual storage account name
account_url = "https://<storage-account-name>.blob.core.windows.net"
# Storage Access Key
shared_access_key = os.getenv("AZURE_STORAGE_ACCESS_KEY")
# 接続先文字列
connection_string = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
# コンテナ名
container_name = os.getenv("AZURE_STORAGE_CONTAINER_NAME")

# １．クレデンシャル情報を用いて BlobServiceClient を作成する
def get_blob_service_client_account_key():

    # Create the BlobServiceClient object
    credential = shared_access_key
    blob_service_client = BlobServiceClient(account_url, credential=credential)

    return blob_service_client


# ２．接続先文字列を用いて BlobServiceClient を作成する
# 予め環境変数 AZURE_STORAGE_CONNECTION_STRING に接続文字列を設定しておく
# Linuxの場合
# export AZURE_STORAGE_CONNECTION_STRING=""
# 接続文字列は、ストレージアカウント＞アクセスキー で取得する
def get_blob_service_client_connection_string():

    # Create the BlobServiceClient object
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)

    return blob_service_client


# 接続文字列から、BlobServiceClient object を生成
blob_service_client = get_blob_service_client_connection_string()

# Create a local directory to hold blob data
upload_path = "./upload"
if not os.path.exists(upload_path):
    os.mkdir(upload_path)

download_path = "./download"
if not os.path.exists(download_path):
    os.mkdir(download_path)

try:
    # Create a file in the local data directory to upload and download
    local_file_name = str(uuid.uuid4()) + ".txt"
    upload_file_path = os.path.join(upload_path, local_file_name)

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
    print(f"An unexpected error has occurred: {e}")

finally:
    # 必ず実行される処理
    print("Processing completed")

