# fbs specification
root_typeは、tableでないといけない
structの中にtableは含められない
unionには、table/struct/stringしか含められない
pythonの場合、unionには、tableしか含められない
Arraysはtableの中にしか作成できない（structの中には作成できない）

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

# binファイル表示
od ./bin/v_sample14.bin
od -ta ./bin/v_sample14.bin

# deserialize (bin > son)
flatc -o ./json/bin_to_json --json --raw-binary ./schema/sample01.fbs -- ./bin/v_sample01.bin
flatc -o ./json/bin_to_json --json --raw-binary ./schema/sample02.fbs -- ./bin/v_sample01.bin


python3 bin_to_json.py ./bin/v_sample01.bin
python3 json_to_bin.py ./v_sample01.json
python3 bin_to_json.py ./v_sample01.bin
flatc -o ./json/bin_to_json --json --raw-binary ./schema/sample01.fbs -- ./v_sample01.bin

flatc -o ./json/bin_to_json_check --json --raw-binary ./schema/sample01.fbs -- ./v_sample01.bin

# copilot 

以下のようにflatbuffers-compilerに指定するv_sample08.jsonを教えてください。

flatc -o ./bin --binary ./schema/sample.fbs ./json/input_value/v_sample.json

sample.fbsは以下のように定義しています。

namespace MyGame.Sample10;

table TopTable {
    ifielda:int = 100;
    ifieldb:int = 200;
}

root_type TopTable;


# copilot Optional and Required Values

flatbuffes の schemaファイルの書き方について教えてください。
下記のドキュメントにある Default, Optional and Required Values についてです。

https://flatbuffers.dev/flatbuffers_guide_writing_schema.html

Default と Optional と Required Values のそれぞれについて個別に教えてほしいです。


# copilot File identification and extension

flatbuffes の schemaファイルの仕様について解説してください。
下記のドキュメントにある File identification and extension についてです。
概要で説明した上で、実例を交えて解説をお願いします。

https://flatbuffers.dev/flatbuffers_guide_writing_schema.html

# copilot RPC interface declarations

flatbuffes の schemaファイルの仕様について解説してください。
下記のドキュメントにある RPC interface declarations についてです。
概要で説明した上で、実例を交えて解説をお願いします。

https://flatbuffers.dev/flatbuffers_guide_writing_schema.html

# copilot Comments & documentation

flatbuffes の schemaファイルの仕様について解説してください。
下記のドキュメントにある Comments & documentation についてです。
概要で説明した上で、実例を交えて解説をお願いします。

https://flatbuffers.dev/flatbuffers_guide_writing_schema.html

# copilot Attributes

flatbuffes の schemaファイルの仕様について解説してください。
下記のドキュメントにある Attributes についてです。
概要で説明した上で、実例を交えて解説をお願いします。

https://flatbuffers.dev/flatbuffers_guide_writing_schema.html

# copilot JSON Parsing

flatbuffes の schemaファイルの仕様について解説してください。
下記のドキュメントにある JSON Parsing についてです。
概要で説明した上で、実例を交えて解説をお願いします。

https://flatbuffers.dev/flatbuffers_guide_writing_schema.html


# copilot Guidelines

flatbuffes の schemaファイルの仕様について解説してください。
下記のドキュメントにある Guidelines についてです。
概要で説明した上で、実例を交えて解説をお願いします。

https://flatbuffers.dev/flatbuffers_guide_writing_schema.html


# copilot Gotchas

flatbuffes の schemaファイルの仕様について解説してください。
下記のドキュメントにある Gotchas についてです。
概要で説明した上で、実例を交えて解説をお願いします。

https://flatbuffers.dev/flatbuffers_guide_writing_schema.html

