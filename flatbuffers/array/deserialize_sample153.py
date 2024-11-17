import sys

from MySample.Sample153.TopTable import TopTable

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
    length = table1.Table2Length()
    print(length)

if __name__ == '__main__':
    main()
