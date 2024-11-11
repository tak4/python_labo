import flatbuffers

import MySample.Sample150.TopTable
import MySample.Sample150.Struct1

def main():
    builder = flatbuffers.Builder(0)

    offset = MySample.Sample150.Struct1.CreateStruct1(builder, [1, 2, 3])
    print(offset, type(offset))

    MySample.Sample150.TopTable.TopTableStart(builder)
    # MySample.Sample150.TopTable.TopTableAddStructa(builder)
    toptable = MySample.Sample150.TopTable.TopTableEnd(builder)

    # 最終的なバッファを完成させる
    builder.Finish(toptable)
    
    # バッファを取得
    buf = builder.Output()

    # Write the binary data to a file
    with open('serialize_sample150.bin', 'wb') as f:
        f.write(buf)    

if __name__ == '__main__':
    main()
