import glob
import re

with open('error_code_list.txt', 'r') as fn:
    data = fn.read()

wlist = data.split('\n')

flist = glob.glob('evidence/e1/ev_log/**')

for fn in flist:
    with open(fn, 'r') as fn:
        data = fn.read()
        for w in wlist:
            print(fn.name, w)
            m = re.search(w, data)
            if m is not None:
                print('exist {}'.format(m.group()))
