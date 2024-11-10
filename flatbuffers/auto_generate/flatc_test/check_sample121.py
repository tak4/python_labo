import os
import sys

from MySample.Sample121.TopTable import TopTable
from MySample.Sample121.Table1 import Table1
from MySample.Sample121.Table2 import Table2
from MySample.Sample121.Table3 import Table3
from MySample.Sample121.Union1 import Union1
from MySample.Sample121.Union2 import Union2

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
    uniona1_type = toptable.Uniona1Type()
    print(f'uniona1_type : {uniona1_type}')
    if uniona1_type == Union1.tablea1:
        table1 = Table1()
        table1.Init(toptable.Uniona1().Bytes, toptable.Uniona1().Pos)
        unionb1_type = table1.Unionb1Type()
        print(f'unionb1_type : {uniona1_type}')
        if unionb1_type == Union1.tablea1:
            table1 = Table1()
            table1.Init(toptable.Uniona1().Bytes, toptable.Uniona1().Pos)
            union_data = table1.Unionb1()
        if unionb1_type == Union1.tableb2:
            table2 = Table2()
            table2.Init(toptable.Uniona1().Bytes, toptable.Uniona1().Pos)
            union_data = table2.Bfielda2()
        if unionb1_type == Union1.tablec3:
            table3 = Table3()
            table3.Init(toptable.Uniona1().Bytes, toptable.Uniona1().Pos)
            union_data = table3.Lfielda3()
    if uniona1_type == Union1.tableb2:
        table2 = Table2()
        table2.Init(toptable.Uniona1().Bytes, toptable.Uniona1().Pos)
        union_data = table2.Bfielda2()
    if uniona1_type == Union1.tablec3:
        table3 = Table3()
        table3.Init(toptable.Uniona1().Bytes, toptable.Uniona1().Pos)
        union_data = table3.Lfielda3()

    print(union_data)

if __name__ == '__main__':
    main()
