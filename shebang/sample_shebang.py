#!/usr/bin/python3
# shebangを記載した場合、./sample_shebang.py で実行可能になるが、
# その場合、/usr/bin/python3 が固定で使用され、
# 仮想環境を使用していても、/usr/bin/python3が使用され、ライブラリも仮想環境のものは使用されない

import sys
import pkg_resources
import numpy as np

# Pythonバージョンの出力
print("Python version:")
print(sys.version)

# インストールされているライブラリの出力（アルファベット順）
print("\nInstalled packages:")
for dist in sorted(pkg_resources.working_set, key=lambda x: x.project_name.lower()):
    print(f"{dist.project_name} ({dist.version})")

