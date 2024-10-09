import flatbuffers
import os
import sys
from pathlib import Path
sys.path.append(
    os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))))

from MySample.Sample20 import TopTable
from MySample.Sample20 import Struct21
from MySample.Sample20 import Struct22

def main():
    basename_without_ext = os.path.splitext(os.path.basename(__file__))[0]
    bsample_name = basename_without_ext.split('_')[1]
    output_bin = f'../serialize/output/{bsample_name}.bin'
    with open(output_bin, 'rb') as f:
        buf = f.read()
        buf = bytearray(buf)
    
    top_table = TopTable.TopTable.GetRootAsTopTable(buf, 0)

    structa1 = top_table.Struct1()
    ifielda1 = structa1.Ifielda1()
    ifieldb1 = structa1.Ifieldb1()
    ifieldc1 = structa1.Ifieldc1()
    print(ifielda1)
    print(ifieldb1)
    print(ifieldc1)

    # 正しい使い方
    # struct21 = structa1.Struct21(Struct21.Struct21())
    # ifielda21 = struct21.Bfielda21()
    # ifieldb21 = struct21.Bfieldb21()
    # ifieldc21 = struct21.Bfieldc21()
    # print(ifielda21)
    # print(ifieldb21)
    # print(ifieldc21)

    # struct22 = structa1.Struct22(Struct22.Struct22())
    # ifielda22 = struct22.Ifielda22()
    # ifieldb22 = struct22.Ifieldb22()
    # ifieldc22 = struct22.Ifieldc22()
    # print(ifielda22)
    # print(ifieldb22)
    # print(ifieldc22)

    # 誤った使い方
    struct22 = structa1.Struct22(Struct21.Struct21())
    ifielda22 = struct22.Bfielda21()
    ifieldb22 = struct22.Bfielda21()
    ifieldc22 = struct22.Bfielda21()
    print(ifielda22)
    print(ifieldb22)
    print(ifieldc22)

    struct21 = structa1.Struct21(Struct22.Struct22())
    ifielda21 = struct21.Ifielda22()
    ifieldb21 = struct21.Ifielda22()
    ifieldc21 = struct21.Ifielda22()
    print(ifielda21)
    print(ifieldb21)
    print(ifieldc21)


if __name__ == '__main__':
  main()
