import flatbuffers
import os
import sys
from pathlib import Path
sys.path.append(
    os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))))

from MySample.Sample20 import TopTable
from MySample.Sample20 import Struct1
from MySample.Sample20 import Struct21
from MySample.Sample20 import Struct22


def main():

    builder = flatbuffers.Builder(0)

    TopTable.TopTableStart(builder)

    # Pattern A
    struct1 = Struct1.CreateStruct1(builder, 10, 20, 30, 40, 50, 60, 70, 80, 90)
    TopTable.TopTableAddStruct1(builder, struct1)

    # Pattan B
    # Struct2.CreateStruct2(builder, 100, 200, 300)

    sample = TopTable.TopTableEnd(builder)

    builder.Finish(sample)
    
    # Output the buffer data
    buf = builder.Output()

    # Write the binary data to a file
    basename_without_ext = os.path.splitext(os.path.basename(__file__))[0]
    bsample_name = basename_without_ext.split('_')[1]
    output_bin = f'output/{bsample_name}.bin'
    with open(output_bin, 'wb') as f:
        f.write(buf)

if __name__ == '__main__':
  main()
