# 指定したprefixのblobを削除する
import os
import sys
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

# 削除対象blob取得
args = sys.argv
if 1 == len(args):
    print("Usage " + args[0] + " delete blob path")
    sys.exit()
delete_blob_path = sys.argv[1]

# 初期設定
# TODO: Replace <storage-account-name> with your actual storage account name
account_url = "https://<storage-account-name>.blob.core.windows.net"
# Storage Access Key
shared_access_key = os.getenv("AZURE_STORAGE_ACCESS_KEY")
# 接続先文字列
connection_string = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
# コンテナ名
container_name = os.getenv("AZURE_STORAGE_CONTAINER_NAME")

print("AZURE_STORAGE_CONNECTION_STRING=" + connection_string)
print("AZURE_STORAGE_CONTAINER_NAME=" + container_name)

# ２．接続先文字列を用いて BlobServiceClient を作成する
# 予め環境変数 AZURE_STORAGE_CONNECTION_STRING に接続文字列を設定しておく
# Linuxの場合
# export AZURE_STORAGE_CONNECTION_STRING=""
# 接続文字列は、ストレージアカウント＞アクセスキー で取得する
def get_blob_service_client_connection_string():

    # Create the BlobServiceClient object
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)

    return blob_service_client

# blobを削除する
def delete_blob(blob_service_client: BlobServiceClient, container_name: str, blob_name: str):
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)
    blob_client.delete_blob()

# 接続文字列から、BlobServiceClient object を生成
blob_service_client = get_blob_service_client_connection_string()


# List the blobs in the container
container_client = blob_service_client.get_container_client(container=container_name) 
blob_list = container_client.list_blobs()
blob_name_list = []
for blob in blob_list:
    if blob.name.startswith(delete_blob_path):
        blob_name_list.append(blob.name)


# delete blob
print("\ndelete blobs...")
for target_blob in blob_name_list:
    print(target_blob)
    # blob削除
    delete_blob(blob_service_client, container_name, target_blob)
