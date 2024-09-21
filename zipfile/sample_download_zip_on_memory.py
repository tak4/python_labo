import io
import requests
import zipfile

# 実際にファイル作成せず、メモリ上で操作する
# ファイル作成する前のテストなどで利用可能

# ※urlはあえて、改行してみる
url = ('https://github.com/pypa/setuptools/archive/refs/tags/'
       'v75.1.0.zip')

# BytesIO でダウンロードしたzipファイルをメモリ上で操作する
f = io.BytesIO()
r = requests.get(url)
f.write(r.content)

with zipfile.ZipFile(f) as z:
    with z.open('setuptools-75.1.0/LICENSE') as f:
        print(f.read().decode())

