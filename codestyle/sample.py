import datetime

import cstyle
import cstyle.cstyle

a1 = {'key1', 'value1'}
a2 = {'key2',             'value2'}

array1 = [ (x, y) for x in range(10) for y in range(10) ]
print(array1)

array2 = [ x for x in range(10) if x % 2 == 0 ]
print(array2)

sum = cstyle.cstyle.add(10, 20)
print(sum)

print(datetime.datetime.utcnow())
