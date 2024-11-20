#!/bin/bash

filename=$1
echo ${filename}
set -x

# fbs -> json
/home/takashi/develop/flatbuffers/flatbuffers_24_3_25/flatc -o ./json/jsonschema --jsonschema ./schema/${filename}.fbs

# generate
# fbsでincludeが使用されている場合は、下記のようにincludeされる側のfbsファイルの指定も必要
# flatc --python ./schema/sample13.fbs ./schema/include_schema.fbs
/home/takashi/develop/flatbuffers/flatbuffers_24_3_25/flatc --python ./schema/${filename}.fbs

# serialize fbs+jsop > bin
/home/takashi/develop/flatbuffers/flatbuffers_24_3_25/flatc -o ./bin --binary ./schema/${filename}.fbs ./json/input_value/v_${filename}.json

# deserialize bin > son 
/home/takashi/develop/flatbuffers/flatbuffers_24_3_25/flatc -o ./json/bin_to_json --json --raw-binary ./schema/${filename}.fbs -- ./bin/v_${filename}.bin