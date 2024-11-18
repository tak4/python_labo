import sys

from MySample.Sample154.TopTable import TopTable

def main():

    if len(sys.argv) <= 1:
        print('Error!!!')
        return

    bin_filename = sys.argv[1]
    print(sys.argv[1])

    with open(bin_filename, 'rb') as f:
        buf = f.read()
        buf = bytearray(buf)
    hex_representation = ' '.join(f'{byte:02x}' for byte in buf)
    print(hex_representation)

    toptable = TopTable.GetRootAsTopTable(buf, 0)
    struct1 = toptable.Struct1()
    print(struct1)
    try:
        length = struct1.Struct2Length()
        print(length)
    except Exception as e:
        print(f"Error deserializing FlatBuffers: {e}")
        print(f"Buffer size: {len(buf)}")

if __name__ == '__main__':
    main()


# 0c 00 00 00 00 00 06 00 10 00 04 00 06 00 00 00 01 00 00 00 02 00 00 00 03 00 00 00
# 0c 00 00 00 00 00 06 00 14 00 04 00 06 00 00 00 01 00 00 00 02 00 00 00 03 00 00 00 04 00 00 00
# 0c 00 00 00 00 00 06 00 08 00 04 00 06 00 00 00 80 00 00 00
# 0c 00 00 00 00 00 06 00 10 00 04 00 06 00 00 00 01 00 00 00 02 00 00 00 03 00 00 00


# 0c 00 00 00 00 00 06 00 10 00 04 00 06 00 00 00 01 00 00 00 02 00 00 00 03 00 00 00
# 0c 00 00 00 00 00 06 00 0a 00 04 00 06 00 00 00 0c 00 00 00 00 00 06 00 08 00 04 00 06 00 00 00 04 00 00 00 03 00 00 00 01 00 00 00 02 00 00 00 03 00 00 00