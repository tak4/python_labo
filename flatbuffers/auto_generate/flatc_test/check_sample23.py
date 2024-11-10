import sys
import struct
import numpy as np

from MySample.Sample23.TopTable1 import TopTable1

# 符号なし整数に変換
def trans_unsigned(field_value):
    unsigned_value = 0

    if field_value < 0:
        unsigned_value = field_value + (1 << 32)
    else: 
        unsigned_value = field_value
    
    return unsigned_value

def main():

    if len(sys.argv) <= 1:
        print('Error!!!')
        return

    bin_filename = sys.argv[1]
    print(sys.argv[1])

    with open(bin_filename, 'rb') as f:
        buf = f.read()
        buf = bytearray(buf)
    print(buf)

    toptable = TopTable1.GetRootAsTopTable1(buf, 0)

    # ドキュメント int
    # https://docs.python.org/ja/3.13/library/functions.html#int
    value = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
    print(f'{type(value)} : {value} hex:{hex(value)}')
    print()

    field_value = toptable.I8()
    print(f'{field_value} {hex(field_value)} {type(field_value)}')
    numpy_value = np.array([trans_unsigned(field_value)], dtype=np.int8)[0]
    print(f'{numpy_value} {hex(numpy_value)} {type(numpy_value)}')

    field_value = toptable.Ui8()
    print(f'{field_value} {hex(field_value)} {type(field_value)}')
    numpy_value = np.array([trans_unsigned(field_value)], dtype=np.uint8)[0]
    print(f'{numpy_value} {hex(numpy_value)} {type(numpy_value)}')

    field_value = toptable.I16()
    print(f'{field_value} {hex(field_value)} {type(field_value)}')
    numpy_value = np.array([trans_unsigned(field_value)], dtype=np.int16)[0]
    print(f'{numpy_value} {hex(numpy_value)} {type(numpy_value)}')

    field_value = toptable.Ui16()
    print(f'{field_value} {hex(field_value)} {type(field_value)}')
    numpy_value = np.array([trans_unsigned(field_value)], dtype=np.uint16)[0]
    print(f'{numpy_value} {hex(numpy_value)} {type(numpy_value)}')

    field_value = toptable.I32()
    print(f'{field_value} {hex(field_value)} {type(field_value)}')
    numpy_value = np.array([trans_unsigned(field_value)], dtype=np.int32)[0]
    print(f'{numpy_value} {hex(numpy_value)} {type(numpy_value)}')

    field_value = toptable.Ui32()
    print(f'{field_value} {hex(field_value)} {type(field_value)}')
    numpy_value = np.array([trans_unsigned(field_value)], dtype=np.uint32)[0]
    print(f'{numpy_value} {hex(numpy_value)} {type(numpy_value)}')

    field_value = toptable.I64()
    print(f'{field_value} {hex(field_value)} {type(field_value)}')
    numpy_value = np.array([trans_unsigned(field_value)], dtype=np.int64)[0]
    print(f'{numpy_value} {hex(numpy_value)} {type(numpy_value)}')

    field_value = toptable.Ui64()
    print(f'{field_value} {hex(field_value)} {type(field_value)}')
    numpy_value = np.array([trans_unsigned(field_value)], dtype=np.uint64)[0]
    print(f'{numpy_value} {hex(numpy_value)} {type(numpy_value)}')

    # unsigned_value = toptable.Ifielda() & 0xFFFFFFFF # マスクして32ビットに制限
    # unsigned_value = struct.unpack('I', struct.pack('I', toptable.Ifielda()))[0]


if __name__ == '__main__':
    main()
