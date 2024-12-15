import os
import re
import sys

if len(sys.argv) < 2:
    print('no input file...')
    sys.exit()

target_path = sys.argv[1]
if os.path.isdir(target_path):
    print('path is dir...')
    sys.exit()

with open('error_code_list.txt', 'r') as fn:
    data = fn.read()
wlist = data.split('\n')

with open(target_path, 'r') as f:
    data = f.read()
    for w in wlist:
        print(f.name, w)
        m = re.findall(w, data)
        for w in m:
            print('exist {}'.format(w))
