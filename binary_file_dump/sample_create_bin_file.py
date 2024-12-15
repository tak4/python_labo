# dump検証用のバイナリファイルを作成する
bin_data = bytes([0x41, 0x42, 0x43])

with open('sample.bin', 'wb') as f:
    f.write(bin_data)
