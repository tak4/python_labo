import os
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

# Create a local directory to hold blob data
download_path = "./download"
if not os.path.exists(download_path):
    os.mkdir(download_path)

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


# List the blobs in the container
print("\nListing blobs...")

container_client = blob_service_client.get_container_client(container=container_name) 
blob_list = container_client.list_blobs()
latest_blob = None
for blob in blob_list:
    print("\t" + blob.name, blob.last_modified)
    if latest_blob is None or blob.last_modified > latest_blob.last_modified:
        latest_blob = blob

print("latest_blob.name : " + latest_blob.name)

# ファイル名とパスを分離
basename = os.path.basename(latest_blob.name)
dirname = os.path.dirname(latest_blob.name)
print(basename)
print(dirname)

# ダウンロードするファイルのディレクトリを再帰的に作成
download_path = os.path.join(download_path, dirname)
if not os.path.exists(download_path):
    os.makedirs(download_path)  # 再帰的にディレクトリ作成

print(download_path)
print(latest_blob.name)

# Download the blob to a local file
# Add 'DOWNLOAD' before the .txt extension so you can see both files in the data directory
download_file_path = os.path.join(download_path, str.replace(basename ,'.txt', '_DOWNLOAD.txt'))
print("\nDownloading blob to \n\t" + download_file_path)

with open(file=download_file_path, mode="wb") as download_file:
    download_file.write(container_client.download_blob(blob.name).readall())
