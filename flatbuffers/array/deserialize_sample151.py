import sys

from MySample.Sample151.TopTable import TopTable

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
    table1 = toptable.Table1()
    length = table1.Sint32Length()
    print(length)
    sint32 = [table1.Sint32(i) for i in range(length)]
    print(sint32, type(sint32))
    sint32_numpy = table1.Sint32AsNumpy()
    print(sint32_numpy, type(sint32_numpy))

if __name__ == '__main__':
    main()
