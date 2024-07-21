# document
https://docs.python.org/ja/3/library/pydoc.html

# document google style guide
https://google.github.io/styleguide/
https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings
https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html

# sample_pydocのドキュメントを表示する
python -m pydoc sample_pydoc
pydoc sample_pydoc

# sysモジュールのドキュメントを表示する
python -m pydoc sys
pydoc sys

# sysモジュールのドキュメントをhtml出力する
python -m pydoc -w sys
pydoc -w sys

pydoc -w ./sample_root_pydoc.py
python -m pydoc -w ./sample_root_pydoc.py
python -m pydoc -w sample_root_pydoc

python -m pydoc -w ./test/test_functions.py
pydoc -w ./test/test_functions.py

# ローカルマシンにウェブブラウザから閲覧可能なドキュメントサーバを起動する
python -m pydoc -p 1234
pydoc -p 1234
