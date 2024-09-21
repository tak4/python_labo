import requests
import tempfile
import zipfile


# 実際にファイル作成せず、メモリ上で操作する
# ファイル作成する前のテストなどで利用可能

# ※urlはあえて、改行してみる
url = ('https://github.com/pypa/setuptools/archive/refs/tags/'
       'v75.1.0.zip')

# BytesIO でダウンロードしたzipファイルをio buffer上のtempfile上で操作する
# 実際にはファイルは作成されないみたい
r = requests.get(url)

with tempfile.TemporaryFile(mode='wb+') as t:
    t.write(r.content)

    print(t.name)
    with zipfile.ZipFile(t) as z:
        with z.open('setuptools-75.1.0/LICENSE') as f:
            print(f.read().decode())
