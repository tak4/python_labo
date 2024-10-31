import importlib

# モジュール名を文字列として指定
module_name = 'calc_module.calc'

# importlibを使ってモジュールを動的にインポート
module = importlib.import_module(module_name)

# インポートされたモジュールの機能を利用
result = module.add(10, 20)
print(f'add {result}')
