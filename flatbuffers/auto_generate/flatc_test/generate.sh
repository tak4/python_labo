#!/bin/bash

filename=$1
echo ${filename}
set -x

# fbs -> json
flatc -o ./json/jsonschema --jsonschema ./schema/${filename}.fbs
flatc -o ./json/jsonschema_strict-json --jsonschema --strict-json ./schema/${filename}.fbs

# generate
flatc --python ./schema/${filename}.fbs

# serialize fbs+jsop > bin
flatc -o ./bin --binary ./schema/${filename}.fbs ./json/input_value/v_${filename}.json

# deserialize bin > son 
flatc -o ./json/bin_to_json --json --raw-binary ./schema/${filename}.fbs -- ./bin/v_${filename}.bin