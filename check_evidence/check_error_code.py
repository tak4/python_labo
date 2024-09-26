import glob
import re

with open('error_code_list.txt', 'r') as f:
    data = f.read()

wlist = data.split('\n')

flist = glob.glob('evidence/e1/ev_log/**')

for f in flist:
    with open(f, 'r') as f:
        data = f.read()
        for w in wlist:
            print(f.name, w)
            m = re.search(w, data)
            if m is not None:
                print('exist {}'.format(m.group()))
