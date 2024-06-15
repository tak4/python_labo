# ファイルのバックアップ
import datetime
import os
import shutil

file_name = 'backup_test.txt'
now = datetime.datetime.now()

if os.path.exists(file_name):
    shutil.copy(file_name, "{}.{}".format(
        file_name, now.strftime('%Y_%m_%d_%H_%M_%S')
    ))

with open(file_name, 'w') as f:
    f.write('test')
