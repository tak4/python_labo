# PyQt6 : GUI フレームワーク
https://pypi.org/project/PyQt6/

# pyinstaller : EXE化
https://pypi.org/project/pyinstaller/

## 実行
python -m executor.impl.dlt_merger.main

## EXE作成
pyinstaller --onefile --noconsole main.py
pyinstaller --onefile --noconsole --name executor --paths . executor/impl/searcher_use_config_yaml/main.py
pyinstaller --onefile --noconsole --name dlt_merger --paths . executor/impl/dlt_merger/main.py

【オプションの解説】  
--onefile: 関連するライブラリやPyQt6のデータをすべて1つの .exe ファイルにまとめます。  
--noconsole: アプリ起動時に、後ろに黒い画面（コマンドプロンプト）が出ないようにします（GUIアプリでは必須レベルのオプションです

