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
    print(buf)

    toptable = TopTable.GetRootAsTopTable(buf, 0)
    tablea = toptable.Tablea()
    length = tablea.Sint32Length()
    print(length)
    sint32 = [tablea.Sint32(i) for i in range(length)]
    print(sint32, type(sint32))
    sint32_numpy = tablea.Sint32AsNumpy()
    print(sint32_numpy, type(sint32_numpy))

if __name__ == '__main__':
    main()
