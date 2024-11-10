import os
import sys

from MySample.Sample21.TopTable import TopTable
from MySample.Sample21.Table1 import Table1
from MySample.Sample21.Table2 import Table2
from MySample.Sample21.Table3 import Table3
from MySample.Sample21.Union1 import Union1

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
    union_type = toptable.UnionaType()
    print(f'union_type : {union_type}')
    if union_type == Union1.tablea1:
        table1 = Table1()
        table1.Init(toptable.Uniona().Bytes, toptable.Uniona().Pos)
        union_data = table1.Ifielda1()
    if union_type == Union1.tableb2:
        table2 = Table2()
        table2.Init(toptable.Uniona().Bytes, toptable.Uniona().Pos)
        union_data = table2.Bfielda2()
    if union_type == Union1.tablec3:
        table3 = Table3()
        table3.Init(toptable.Uniona().Bytes, toptable.Uniona().Pos)
        union_data = table3.Lfielda3()

    print(union_data)

if __name__ == '__main__':
    main()
