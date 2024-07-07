import os
import sys

from test_ext_function.utility import Environment

# カレントディレクトリ(=pytestを実行したディレクトリという想定)を取得
pytest_dir = os.getcwd()

# ライブラリの参照ディレクトリを追加
# test_ext_function.py から、
# テスト対象の helper.testing_utils を参照する為に必要
sys.path.append(pytest_dir)
# ライブラリの参照ディレクトリは下記で確認可能
# print(sys.path)

# setting/setting.yaml をテストコードで参照する試み
Environment.read_setting(pytest_dir + '/setting/setting.yaml')
