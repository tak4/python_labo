import flatbuffers
import MySample.Sample154.TopTable
import MySample.Sample154.Table1
import MySample.Sample154.Struct1


def serialize_to_flatbuffer(data):
    builder = flatbuffers.Builder(0)

    struct1 = MySample.Sample154.Struct1.CreateStruct1(builder, 100)

    table1 = MySample.Sample154.Table1.CreateTable1(builder, [struct1, struct1, struct1])

    MySample.Sample154.TopTable.TopTableStart(builder)
    MySample.Sample154.TopTable.TopTableAddTable1(builder, table1)
    toptable = MySample.Sample154.TopTable.TopTableEnd(builder)

    # # Struct1の作成
    # struct1_list = []
    # for struct_data in data['struct1_data']:
    #     struct1 = schema_generated.CreateStruct1(builder, struct_data['sint32'])
    #     struct1_list.append(struct1)

    # # Table1の作成
    # table1 = schema_generated.CreateTable1(builder, struct1_list)

    # # TopTableの作成
    # schema_generated.TopTableStart(builder)
    # schema_generated.TopTableAddTable1(builder, table1)
    # top_table = schema_generated.TopTableEnd(builder)

    # # バッファの終了
    builder.Finish(toptable)

    # バッファを取得
    buf = builder.Output()

    return buf

# シリアライズするデータ
data = {
    'struct1_data': [
        {'sint32': 10},
        {'sint32': 20},
        {'sint32': 30},
    ]
}

# FlatBuffersデータを作成
flatbuffer = serialize_to_flatbuffer(data)

# ファイルに保存
with open('serialize_sample154.bin', 'wb') as f:
    f.write(flatbuffer)