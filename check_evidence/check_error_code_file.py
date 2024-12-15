import glob
import re
import sys

if sys.argv < 2:
    print('no input file...')

with open('error_code_list.txt', 'r') as f:
    data = f.read()

wlist = data.split('\n')

flist = glob.glob('evidence/e1/ev_log/**')

with open(f, 'r') as f:
    data = f.read()
    for w in wlist:
        print(f.name, w)
        m = re.search(w, data)
        if m is not None:
            print('exist {}'.format(m.group()))
