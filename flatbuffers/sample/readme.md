# flatbuffers 公式サイト

https://flatbuffers.dev/

## flatbuffers チュートリアル
https://flatbuffers.dev/flatbuffers_guide_tutorial.html


## github / clone

https://github.com/google/flatbuffers

git clone https://github.com/google/flatbuffers.git


## ビルド

clone したディレクトリ以下にて以下を実行
cmake -G "Unix Makefiles"
make -j


## スキーマファイルのコンパイル

../flatbuffers/flatc --python monster.fbs


## ビルドせずにインストール

apt インストール
sudo apt install flatbuffers-compiler

snap インストール
sudo snap install flatbuffers


## serialize / deserialize

チュートリアル
python_labo/flatbuffers/sample/sample_binary.py

シリアライズ　チュートリアルのSourceから分離
python_labo/flatbuffers/sample/serialize.py
python3 serialize.py

デシリアライズ　チュートリアルのSourceから分離
python_labo/flatbuffers/sample/deserialize.py
python3 deserialize.py
