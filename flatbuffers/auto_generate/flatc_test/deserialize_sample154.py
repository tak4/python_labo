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
    print(buf)

    toptable = TopTable.GetRootAsTopTable(buf, 0)
    table1 = toptable.Table1()

    try:
        length = table1.Struct1Length()
        print(length)
    except Exception as e:
        print(f"Error deserializing FlatBuffers: {e}")
        print(f"Buffer size: {len(buf)}")

if __name__ == '__main__':
    main()
