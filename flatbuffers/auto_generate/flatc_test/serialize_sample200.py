import flatbuffers

import MySample.Sample200.TopTable

def main():
    builder = flatbuffers.Builder(0)

    MySample.Sample200.TopTable.TopTableStart(builder)
    toptable = MySample.Sample200.TopTable.TopTableEnd(builder)

    # 最終的なバッファを完成させる
    builder.Finish(toptable)
    
    # バッファを取得
    buf = builder.Output()

    # Write the binary data to a file
    with open('serialize_sample200.bin', 'wb') as f:
        f.write(buf)    

if __name__ == '__main__':
    main()
