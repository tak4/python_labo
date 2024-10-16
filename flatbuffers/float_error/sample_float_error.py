# pythonのfloatは、
f = float(0.1)
print(f)
f = 0.1
print(f)


decimal_number = 10
binary_number = bin(decimal_number)
print('{}'.format(binary_number))  # 結果は '0b1010' となります


print(int(100), hex(100), oct(100), bin(100))
print('{0:d} {0:#x} {0:#o} {0:#b}'.format(100))
print('{0:d} {0:x} {0:o} {0:b}'.format(100))    # 0x 0o 0b 表記無し



def decimal_to_binary(decimal_number):
    # 整数部分を2進数に変換
    integer_part = int(decimal_number)
    binary_integer_part = bin(integer_part).lstrip("0b")

    # 小数部分を2進数に変換
    fractional_part = decimal_number - integer_part
    binary_fractional_part = []
    while fractional_part:
        fractional_part *= 2
        bit = int(fractional_part)
        binary_fractional_part.append(str(bit))
        fractional_part -= bit
        if len(binary_fractional_part) > 10:  # 適当な桁数で止める
            break

    return f"{binary_integer_part}.{''.join(binary_fractional_part)}"

decimal_number = 0.1
binary_number = decimal_to_binary(decimal_number)
print(binary_number)  # 結果は '1010.101' となります
