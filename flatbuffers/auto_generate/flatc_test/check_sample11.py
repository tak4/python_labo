import os
import sys

from MySample.Sample11.TopTable import TopTable

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
    ifielda = toptable.Ifielda()
    ifieldb = toptable.Ifieldb()
    print(ifielda)
    print(ifieldb)

if __name__ == '__main__':
    main()
