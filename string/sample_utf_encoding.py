# 'あ'をunicode, utfで確認
s = 'あ'
print(s)

# unicodeに変換
unicode = ord(s)
print(unicode)

# utf-8 にエンコード
# 特徴: 可変長エンコーディング方式で、1バイトから4バイトまでの長さで文字を表現します。
# 用途: ウェブページやインターネット通信で広く使用されています。ASCIIとの互換性があり、効率的なエンコーディングが可能です1。
u8 = s.encode('utf-8')
print("s.encode('utf-8')", u8)
bu8 = bytes(s, 'utf-8')
print("bytes(s, 'utf-8')", bu8)

s8 = u8.decode('utf-8')
print("s32.decode('utf-8')", s8)
bs8 = bu8.decode('utf-8')
print("bs32.decode('utf-8')", bs8)

# utf-16 にエンコード
# 特徴: 固定長または可変長エンコーディング方式で、基本的には2バイト（16ビット）で文字を表現しますが、一部の文字は4バイト（32ビット）で表現されます。
# 用途: WindowsやJavaなどのプラットフォームで広く使用されています。多くの現代の言語を効率的にエンコードできます2。
u16 = s.encode('utf-16')
print("s.encode('utf-16')", u16)
bu16 = bytes(s, 'utf-16')
print("bytes(s, 'utf-16')", bu16)

s16 = u16.decode('utf-16')
print("s32.decode('utf-16')", s16)
bs16 = bu16.decode('utf-16')
print("bs32.decode('utf-16')", bs16)

# utf-32 にエンコード
# 特徴: 固定長エンコーディング方式で、すべての文字を4バイト（32ビット）で表現します。
# 用途: メモリ効率よりもアクセスの簡便さが求められるシステムで使用されます。全ての文字が同じ長さで表現されるため、ランダムアクセスが容易です2。
u32 = s.encode('utf-32')
print("s.encode('utf-32')", u32)
bu32 = bytes(s, 'utf-32')
print("bytes(s, 'utf-32')", bu32)

s32 = u32.decode('utf-32')
print("s32.decode('utf-32')", s32)
bs32 = bu32.decode('utf-32')
print("bs32.decode('utf-32')", bs32)
