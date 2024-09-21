import glob
import os
import pathlib
import zipfile

#
# zip化対象ファイル作成
#
file1 = 'test_dir/test.txt'
file2 = 'test_dir/sub_dir/sub_test.txt'
file3 = 'test_dir/sub_dir/subsub_dir/sub_sub_test.txt'

os.makedirs('test_dir/sub_dir/subsub_dir', exist_ok=True)

# touch 無くても、後のwriteでファイル作成される
pathlib.Path(file1).touch()
pathlib.Path(file2).touch()

with open(file1, 'w') as f:
    f.write('test')

with open(file2, 'w') as f:
    f.write('sub')

with open(file3, 'w') as f:
    f.write('subsub')

#
# zip圧縮
#
os.makedirs('output', exist_ok=True)

# ディレクトリ、ファイル個別にwriteしないとzipに含まれない
# with zipfile.ZipFile('output/test.zip', 'w') as z:
#     z.write('test_dir')
#     z.write('test_dir/test.txt')

# 全てのファイルを対象にzip作成
with zipfile.ZipFile('output/test.zip', 'w') as z:
    for f in glob.glob('test_dir/**', recursive=True):
        z.write(f)


#
# zip展開
#
with zipfile.ZipFile('output/test.zip', 'r') as z:
    with z.open('test_dir/test.txt') as f:
        print(f.read())

with zipfile.ZipFile('output/test.zip', 'r') as z:
    z.extractall('test_zip')