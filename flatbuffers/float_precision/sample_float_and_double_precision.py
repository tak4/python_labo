import struct

# 浮動小数点
# https://medium-company.com/%e6%b5%ae%e5%8b%95%e5%b0%8f%e6%95%b0%e7%82%b9%e6%95%b0/
# 浮動小数点数内部表現シミュレーター
# https://tools.m-bsys.com/calculators/ieee754.php

# bytes
# https://docs.python.org/ja/3/library/stdtypes.html#bytes
# struct
# https://docs.python.org/ja/3/library/struct.html#module-struct

# 元の値
# IEEE754「1.××」の形で正規化されている
original_decimal_number = 0.1
print(original_decimal_number)

#
# original_decimal_numberを32bit 16進、2進数表示に変換する
#

# バイト列オブジェクトに変換する
# ">f"：ビッグエンディアン／float
binary_data = struct.pack(">f", original_decimal_number)
print(binary_data)

# 16進数表示 1byteずつスペースで区切る
hex_representation = ' '.join(f'{byte:02x}' for byte in binary_data)
print(hex_representation)

# 2進数表示 1byteずつスペースで区切る
binary_representation = ' '.join(f'{byte:08b}' for byte in binary_data)
print(binary_representation)
# 00111101 11001100 11001100 11001101
#   符号(1bit)   ： 0
#   指数部(8bit) ： 01111011 バイアス127を引いて、-4 を示す
#   仮数部(23bit)： 1001100 11001100 11001101
# 1.0011001100110011001101 * 2^-4
# 0.00010011001100110011001101

#
# 2進数表示データを10進表示に変換する
#

# 2進数データを16進数データに変換
byte_data = bytes(int(b, 2) for b in binary_representation.split())
print(byte_data)

# 16進数表示 1byteずつスペースで区切る
hex_representation = ' '.join(f'{byte:02x}' for byte in byte_data)
print(hex_representation)

# バイトデータをfloatに変換する
decimal_number = struct.unpack('>f', byte_data)[0]
print(decimal_number)

print()

#
# original_decimal_numberを64bit 16進、2進数表示に変換する
#

# バイト列オブジェクトに変換する
# ">d"：ビッグエンディアン／double
binary_data = struct.pack(">d", original_decimal_number)
print(binary_data)

# 16進数表示 1byteずつスペースで区切る
hex_representation = ' '.join(f'{byte:02x}' for byte in binary_data)
print(hex_representation)

# 2進数表示 1byteずつスペースで区切る
binary_representation = ' '.join(f'{byte:08b}' for byte in binary_data)
print(binary_representation)
# 00111111 10111001 10011001 10011001 10011001 10011001 10011001 10011010
# 符号(1bit)   ： 0
# 指数部(11bit)： 01111111011 バイアス1023を引いて、-4 を示す
# 仮数部(23bit)： 1001 10011001 10011001 10011001 10011001 10011001 10011010
# 1.001100110011001100110011001100110011001100110011010 * 2^-4
# 0.0001001100110011001100110011001100110011001100110011010

#
# 2進数表示データを10進表示に変換する
#

# 2進数データを16進数データに変換
byte_data = bytes(int(b, 2) for b in binary_representation.split())
print(byte_data)

# 16進数表示 1byteずつスペースで区切る
hex_representation = ' '.join(f'{byte:02x}' for byte in byte_data)
print(hex_representation)

# バイトデータを浮動小数点数に変換する
decimal_number = struct.unpack('>d', byte_data)[0]
print(decimal_number)

