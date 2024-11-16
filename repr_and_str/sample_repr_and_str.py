# reprとstr
# reqr representation 表示

print('s')
print(str('s'))     # 's'と同じ
print(repr('s'))    # Pythonオブジェクトとして表示
print()

import datetime
d = datetime.datetime.now()
print(d)
print(str(d))
print(repr(d))
print()

# format指定によるrepr
print('{!r} {} {!s}'.format('test', 'test1', 'test2'))
print()

class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return 'Point<object>'

    def __str__(self):
        return 'Point ({}, {})'.format(self.x, self.y)

p = Point(10, 20)
print('{0!r}'.format(p))
print('{0}'.format(p))
print('{0!s}'.format(p))
