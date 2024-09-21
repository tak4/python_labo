import requests
import tempfile
import zipfile


# 実際にファイル作成せず、メモリ上で操作する
# ファイル作成する前のテストなどで利用可能

# ※urlはあえて、改行してみる
url = ('https://github.com/pypa/setuptools/archive/refs/tags/'
       'v75.1.0.zip')

r = requests.get(url)
with open('download.zip', 'wb') as f:
    f.write(r.content)
