#!/bin/bash

# 現在の状態を判断し、実行するコマンドを決定
if [ -f enable_flatc.1.12.0 ]; then
  # enable_flatc.1.12.0 が存在する場合
  rm -rf enable_flatc.1.12.0
  target_version="24.3.25"
  create_file="enable_flatc.24.3.25"
elif [ -f enable_flatc.24.3.25 ]; then
  # enable_flatc.24.3.25 が存在する場合
  rm -rf enable_flatc.24.3.25
  target_version="1.12.0"
  create_file="enable_flatc.1.12.0"
else
  target_version="1.12.0"
  create_file="enable_flatc.1.12.0"
fi

# 現在のディレクトリを保存
original_dir=$(pwd)
# /usr/bin ディレクトリへ移動
cd /usr/bin

# シンボリックリンクの作成
sudo ln -sf flatc.$target_version flatc

# 元のディレクトリに戻る
cd "$original_dir"

# ファイルの作成
touch $create_file

echo "flatc linked to flatc.$target_version in /usr/bin"
echo "$create_file created"
