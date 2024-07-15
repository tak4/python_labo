# Schema ファイルコンパイル

flatc --python ./schema/Human.fbs

# path

export PYTHONPATH=".:$PYTHONPATH"

# 実行
python3 ./serializer/human/serialize_human.py

python3 ./deserializer/human/deserialize_json_human.py
python3 ./deserializer/human/deserialize_bin_human.py


parse json
base64
deserialize
generate json
