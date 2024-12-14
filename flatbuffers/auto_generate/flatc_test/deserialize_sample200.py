import sys

from MySample.Sample200.TopTable import TopTable
from MySample.Sample200.Table1 import Table1
from MySample.Sample200.Table2 import Table2
from MySample.Sample200.Union1 import Union1

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

    toptable = TopTable.GetRootAs(buf, 0)
    bfeilda = toptable.Bfeilda()
    ubfeilda = toptable.Ubfeilda()
    bofielda = toptable.Bofielda()
    sfielda = toptable.Sfielda()
    usfielda = toptable.Usfielda()
    ifielda = toptable.Ifielda()
    uifielda = toptable.Uifielda()
    ffielda = toptable.Ffielda()
    lfielda = toptable.Lfielda()
    ulfield = toptable.Ulfielda()
    dfielda = toptable.Dfielda()
    strfielda= toptable.Strfielda()

    print(f'bfeilda: {bfeilda}')
    print(f'ubfeilda:{ubfeilda}')
    print(f'bofielda:{bofielda}')
    print(f'sfielda:{sfielda}')
    print(f'usfielda:{usfielda}')
    print(f'ifielda:{ifielda}')
    print(f'uifielda:{uifielda}')
    print(f'ffielda:{ffielda}')
    print(f'lfielda:{lfielda}')
    print(f'ulfield:{ulfield}')
    print(f'dfielda:{dfielda}')
    print(f'strfielda:{strfielda}')

    tbfielda = toptable.Tbfielda()
    if tbfielda is not None:
        tbfielda_bfeilda = tbfielda.Bfeilda()
        tbfielda_stfielda = tbfielda.Stfielda()
        print(f'tbfielda_bfeilda:{tbfielda_bfeilda}')
        print(f'tbfielda_stfielda:{tbfielda_stfielda}')

    stfielda = toptable.Stfielda()
    if stfielda is not None:
        stfielda_bfeilda = stfielda.Bfeilda()
        stfielda_bofielda = stfielda.Bofielda()
        print(f'stfielda_bfeilda:{stfielda_bfeilda}')
        print(f'stfielda_bofielda:{stfielda_bofielda}')

    unfielda_type = toptable.UnfieldaType()
    if unfielda_type == Union1.NONE:
        print('unfielda_type is NONE')
    elif unfielda_type == Union1.Table1:
        table1 = Table1()
        table1.Init(toptable.Unfielda().Bytes, toptable.Unfielda().Pos)
        unfielda_bfeilda = table1.Bfeilda()
        unfielda_stfielda = table1.Stfielda()
        print(f'unfielda_bfeilda:{unfielda_bfeilda}')
        print(f'unfielda_stfielda:{unfielda_stfielda}')
    elif unfielda_type == Union1.Table2:
        table2 = Table2()
        table2.Init(toptable.Unfielda().Bytes, toptable.Unfielda().Pos)
        unfielda_bofielda = table2.Bofielda()
        unfielda_sfielda = table2.Sfielda()
        print(f'unfielda_bofielda:{unfielda_bofielda}')
        print(f'unfielda_sfielda:{unfielda_sfielda}')

    enfielda = toptable.Enfielda()
    print(f'enfielda:{enfielda}')

    alfielda= [toptable.Alfielda(i) for i in range(toptable.AlfieldaLength())]
    print(f'alfielda:{alfielda}')
    alfielda_as_numpy = toptable.AlfieldaAsNumpy()
    print(f'alfielda_as_numpy:{alfielda_as_numpy}')


if __name__ == '__main__':
    main()
