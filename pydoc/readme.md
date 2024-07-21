# document
https://docs.python.org/ja/3/library/pydoc.html

# sample_pydocのドキュメントを表示する
python -m pydoc sample_pydoc
pydoc sample_pydoc

# sysモジュールのドキュメントを表示する
python -m pydoc sys
pydoc sys

# sysモジュールのドキュメントをhtml出力する
python -m pydoc -w sys
pydoc -w sys

pydoc ./sample_root_pydoc.py
python -m pydoc ./sample_root_pydoc.py
python -m pydoc sample_root_pydoc

python -m pydoc ./test/test_functions.py
pydoc ./test/test_functions.py

# ローカルマシンにウェブブラウザから閲覧可能なドキュメントサーバを起動する
python -m pydoc -p 1234
pydoc -p 1234
