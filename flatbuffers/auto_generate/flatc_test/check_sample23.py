import sys
import struct
import numpy as np

from MySample.Sample10.TopTable import TopTable

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
    # unsigned_value = toptable.Ifielda()
    unsigned_value = toptable.Ifielda() & 0xFFFFFFFF # マスクして32ビットに制限
    # unsigned_value = struct.unpack('I', struct.pack('I', toptable.Ifielda()))[0]
    # unsigned_value = np.array([toptable.Ifielda()], dtype=np.uint32)
    print(unsigned_value)

if __name__ == '__main__':
    main()
