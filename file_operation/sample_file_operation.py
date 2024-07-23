import os
import shutil

# 複数階層のディレクトリ作成
# exist_ok=True：既にディレクトリあってもエラーにしない
os.makedirs('./temp_work/temp', exist_ok=True)

# ディレクトリを中身ごと消す
# shutil.rmtree() ではディレクトリが無いときエラーになる
# 存在チェックをしてから削除する
if os.path.isdir('./temp_work'):
    shutil.rmtree('./temp_work')
