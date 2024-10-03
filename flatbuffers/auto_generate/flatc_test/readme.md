# fbs -> json
flatc -o ./json/jsonschema --jsonschema ./schema/sample01.fbs
flatc -o ./json/jsonschema_strict-json --jsonschema --strict-json ./schema/sample01.fbs

flatc -o ./json/jsonschema --jsonschema ./schema/sample02.fbs
flatc -o ./json/jsonschema_strict-json --jsonschema --strict-json ./schema/sample02.fbs


# generate
flatc --python ./schema/sample01.fbs
flatc --python ./schema/sample02.fbs

# serialize (fbs+jsop > bin)
flatc -o ./bin --binary ./schema/sample01.fbs ./json/input_value/v_sample01.json
flatc -o ./bin --binary ./schema/sample02.fbs ./json/input_value/v_sample02.json
flatc -o ./bin --binary ./schema/sample03.fbs ./json/input_value/v_sample03.json

# deserialize (bin > son)
flatc -o ./json/bin_to_json --json --raw-binary ./schema/sample01.fbs -- ./bin/v_sample01.bin
flatc -o ./json/bin_to_json --json --raw-binary ./schema/sample02.fbs -- ./bin/v_sample01.bin


python3 bin_to_json.py ./bin/v_sample01.bin
python3 json_to_bin.py ./v_sample01.json
python3 bin_to_json.py ./v_sample01.bin
flatc -o ./json/bin_to_json --json --raw-binary ./schema/sample01.fbs -- ./v_sample01.bin

flatc -o ./json/bin_to_json_check --json --raw-binary ./schema/sample01.fbs -- ./v_sample01.bin
