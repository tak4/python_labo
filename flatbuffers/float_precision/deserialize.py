from decimal import Decimal

from Sample.TopTable import TopTable

def main():

    with open('output.bin', 'rb') as f:
        buf = f.read()
        buf = bytearray(buf)

    hex_representation = ' '.join(f'{byte:02x}' for byte in buf)
    print(hex_representation)

    toptable = TopTable.GetRootAsTopTable(buf, 0)
    fv = toptable.FVal()
    dv = toptable.DVal()

    print(f'flatbuffres fv={fv}')
    print(f'flatbuffres dv={dv}')


if __name__ == '__main__':
    fv = float(0.1)
    print(f'python fv={fv} {type(fv)}')

    main()
