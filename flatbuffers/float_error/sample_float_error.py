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
