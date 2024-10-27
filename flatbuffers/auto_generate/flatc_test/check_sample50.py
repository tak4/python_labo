from MySample.Sample50.TopTable import TopTable

def main():
    with open('bin/v_sample50.bin', 'rb') as f:
        buf = f.read()
        buf = bytearray(buf)
    print(buf)

    toptable = TopTable.GetRootAsTopTable(buf, 0)

    tablea = toptable.Tablea()

    #
    # tablea
    #
    tablea_ifielda = tablea.Ifielda()
    tablea_colora = tablea.Colora()
    tablea_stringa = tablea.Stringa()
    print(f'tablea_ifielda: {tablea_ifielda}')
    print(f'tablea_colora: {tablea_colora}')
    print(f'tablea_stringa: {tablea_stringa}')
    
    #
    # tableb
    #
    # input/v_sample50.json によるtablebの値指定が無い場合、tablebはNoneとなる
    # tableb = toptable.Tableb()
    # tableb_ifielda = tableb.Ifielda()
    # tableb_colora = tableb.Colora()
    # tableb_stringa = tableb.Stringa()
    # print(f'tableb_ifielda: {tableb_ifielda}')
    # print(f'tableb_colora: {tableb_colora}')
    # print(f'tableb_stringa: {tableb_stringa}')

    #
    # structa
    #
    structa = toptable.Structa()
    structa_ifielda = structa.Ifielda()
    structa_colora = structa.Colora()
    print(f'structa_ifielda: {structa_ifielda}')
    print(f'structa_colora: {structa_colora}')

    #
    # structb
    #
    # input/v_sample50.json によるstructbの値指定が無い場合、structbはNoneとなる
    # structb = toptable.Structb()
    # structb_ifielda = structb.Ifielda()
    # structb_colora = structb.Colora()
    # print(f'structb_ifielda: {structb_ifielda}')
    # print(f'structb_colora: {structb_colora}')

if __name__ == '__main__':
    main()
