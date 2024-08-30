import os
import yaml

# setting/setting.yaml をテストコードで参照する試み
class Environment(object):
    _setting = None

    @classmethod
    def read_setting(cls, setting_file):
        # カレントディレクトリ(=pytestを実行したディレクトリという想定)を取得
        pytest_dir = os.getcwd()
        with open(setting_file, 'r') as yaml_file:
            cls._setting = yaml.safe_load(yaml_file)

    @classmethod
    def get_setting(cls):
        return cls._setting
