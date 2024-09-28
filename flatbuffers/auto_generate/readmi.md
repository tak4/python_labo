
# fbsファイルより、ジェネレータ(Pythonコード)を生成する
flatc --python ./schema/monster.fbs  

# fbsファイルをjsonファイルに変換する
※以下２つの生成物で差異無し　※違いが不明  
flatc -o ./json/jsonschema --jsonschema ./schema/monster.fbs  
flatc -o ./json/jsonschema_strict-json --jsonschema --strict-json ./schema/monster.fbs  

jsonディレクトリ以下に出力

# AITRIOS flatbuffers schema
https://github.com/SonySemiconductorSolutions/aitrios-sdk-vision-sensing-app/tree/main/tutorials/4_prepare_application/1_develop/sdk/schema
