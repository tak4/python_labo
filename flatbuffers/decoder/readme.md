# Schema ファイルコンパイル

flatc --python ./schema/Human.fbs

# path

export PYTHONPATH=".:$PYTHONPATH"

# 実行
python3 ./serializer/human/serialize_human.py

python3 deserializer/human/deserialize_bin_human.py -i ./input/output_human.bin -o ./output/output_human.txt

python3 deserializer/human/deserialize_json_human.py -i ./input/encode_human.json -o ./output/decode_human.json

python3 main.py -k human -i ./input/encode_human.json -o ./output/decode_human.json
