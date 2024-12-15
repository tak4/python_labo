with open('sample.bin', 'rb') as f:
    bin_data = f.read()

# printでそのまま出力すると表示可能なデータは__repr__により文字として表示される
print(bin_data)
# 16進表示、スペースでつなげてメモリダンプ風に出力する
hex_representation = ' '.join(f'{byte:02x}' for byte in bin_data)
print(hex_representation)