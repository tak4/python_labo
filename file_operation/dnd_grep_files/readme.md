# GUI フレームワーク
https://pypi.org/project/PyQt6/

# EXE化
https://pypi.org/project/pyinstaller/

pyinstaller --onefile --noconsole main.py
【オプションの解説】

--onefile: 関連するライブラリやPyQt6のデータをすべて1つの .exe ファイルにまとめます。

--noconsole: アプリ起動時に、後ろに黒い画面（コマンドプロンプト）が出ないようにします（GUIアプリでは必須レベルのオプションです）。
