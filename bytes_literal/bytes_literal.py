
# stringをバイトリテラルに変換
string = "ABC"
print(string, type(string))
byte_literal = string.encode('utf-8')
print(byte_literal, type(byte_literal))
print()

# bでバイトリテラル定義
byte_literal = b"ABC"
print(byte_literal, type(byte_literal))
print()

# bytesでバイトリテラル定義
byte_literal = bytes([0x41, 0x42, 0x43])
print('bytes([0x41, 0x42, 0x43])')
print(byte_literal, type(byte_literal))

# bytesが文字列のように出力されるのは__repr__のため
# https://docs.python.org/ja/3/library/stdtypes.html#bytes
byte_literal = bytes([0x41, 0x42, 0x43]).__repr__()
print('bytes([0x41, 0x42, 0x43]).__repr__()')
print(byte_literal, type(byte_literal))
print('bytes([0x41])')
byte_literal = bytes([0x41])
print(byte_literal, type(byte_literal))
print('bytes([0x41]).__repr__()')
byte_literal = bytes([0x41]).__repr__()
print(byte_literal, type(byte_literal))
print()

byte_literal = bytes([0, 1, 2, 30, 31, 32, 33, 64])
print(byte_literal, type(byte_literal))
# => b'\x00\x01\x02\x1e\x1f !' <class 'bytes'>
# 制御文字部分はそのまま数値出力
# 表示可能文字部分は、表示可能文字で表示される __repr__ の効果らしい
# 00 = 0x00 = Null
# 01 = 0x01 = Start Of Heading
# 02 = 0x02 = Start Of Text
# 30 = 0x1e = Record Separator
# 31 = 0x1f = Unit Separator
# 32 = 0x20 = space
# 33 = 0x21 = exclamation mark
# 34 = 0x22 = quotation mark / double quote / comillas
# 64 = 0x40 = @ commercial at / at sign

