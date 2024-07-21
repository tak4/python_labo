# Tavern

https://tavern.readthedocs.io/en/latest/


## 仮想環境

source ../venv_flask_tavern/bin/activate

## インストール

pip install tavern
pip install azure-storage-blob


## テスト実行

### -v：yamlファイルとnameを表示
pytest -v test_basic

### durations=0：長さが0秒を超えるテストのリストを取得
pytest --durations=0 test_basic

### --tb=short：
pytest --tb=showlocals test_basic

### -p no:logging
pytest --tb=showlocals -p no:logging test_basic