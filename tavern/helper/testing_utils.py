import os
from box import Box
import json
from azure.storage.blob import BlobServiceClient

SAVE_DIR = f"./save/"

def response_test(response):
    j = response.json()
    ret = False
    if j['name'] == "Cannon Wood":
        ret = True
    else:
        ret = False

    return ret

def is_specified_json(response, schema):
    json = response.json()
    assert json.get("name") == schema.get("name"), 'xxxx name error'

def save_response_file(response, fname):
    j = response.json()

    if not os.path.isdir(SAVE_DIR):
        os.mkdir(SAVE_DIR)

    with open(SAVE_DIR + fname, "w") as f:
        # JSONデータを書き出す
        json.dump(j, f)

def disp_response(response, _id):

    if not os.path.isdir(SAVE_DIR):
        os.mkdir(SAVE_DIR)

    with open(f"./save/_id.txt", "w") as f:
        f.write(_id)

def save_response_box(response):
    json = response.json()
    r_name = json.get("name")
    print()
    print('r_name : {}'.format(r_name))

    ret_box = Box({'box_name': r_name, 'box_int_val': 123, 'box_float_val': 123.4})
    print('ret_box.box_name      : {} / {}'.format(ret_box.box_name, type(ret_box.box_name)))
    print('ret_box.box_int_val   : {} / {}'.format(ret_box.box_int_val, type(ret_box.box_int_val)))
    print('ret_box.box_float_val : {} / {}'.format(ret_box.box_float_val, type(ret_box.box_float_val)))

    return ret_box

def disp_response_box(response, name, int_val, float_val):
    print()
    # tavernより渡されてきた変数は、tavern._core.formatted_str.FormattedString という型になる
    print('name      : {} / {}'.format(name, type(name)))
    print('int_val   : {} / {}'.format(int_val, type(int_val)))
    print('float_val : {} / {}'.format(float_val, type(float_val)))


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

def download_azure_blob(response):

    # 接続文字列から、BlobServiceClient object を生成
    blob_service_client = get_blob_service_client_connection_string()

    # コンテナ名
    container_name = "imageanalysis"

    # Create a local directory to hold blob data
    local_path = "./data"
    if not os.path.exists(local_path):
        os.mkdir(local_path)

    try:
        # List the blobs in the container
        container_client = blob_service_client.get_container_client(container=container_name) 
        blob_list = container_client.list_blobs()
        latest_blob = None
        for blob in blob_list:
            if latest_blob is None or blob.last_modified > latest_blob.last_modified:
                latest_blob = blob

        # Download the blob to a local file
        # Add 'DOWNLOAD' before the .txt extension so you can see both files in the data directory
        download_file_path = os.path.join(local_path, str.replace(latest_blob.name ,'.txt', '_DOWNLOAD.txt'))
        container_client = blob_service_client.get_container_client(container=container_name) 

        with open(file=download_file_path, mode="wb") as download_file:
            download_file.write(container_client.download_blob(blob.name).readall())

    except Exception as e:
        print(f"予期しないエラーが発生しました: {e}")

    finally:
        print("処理が完了しました")


def generate_bearer_token():
    token = "abcdefg"
    auth_header = {
        "Authorization": "Bearer {}".format(token)
    }
    return Box(auth_header)



if __name__ == '__main__':
    download_azure_blob()
