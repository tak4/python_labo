import re

with open('../schema/monster.fbs') as f:
    data = f.read()

m = re.search(r'struct\s+(\w+)\s*\{((\s*[\w:\w]+[ ;])+\s*)\}', data, re.MULTILINE)
if m is not None:
    print(m.group(0))
    print(m.group(1))
    print(m.group(2).split('\n'))

m = re.search(r'table\s+(\w+)\s*\{\s*[\w:\[\]]+', data, re.MULTILINE)
if m is not None:
    print(m.group(0))
