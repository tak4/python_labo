import sys

print(sys.getdefaultencoding())

test_string = 'hello world\n'
e_test_string = test_string.encode()
d_test_string = e_test_string.decode()
print('e_test_string', type(e_test_string), e_test_string)
print('d_test_string', type(d_test_string), d_test_string)
print('test_string', type(test_string), test_string)

with open('encode', 'wb') as f:
    f.write(e_test_string)

with open('no_encode', 'w') as f:
    f.write(test_string)