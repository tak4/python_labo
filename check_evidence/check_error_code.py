import glob
import re

with open('error_code_list.txt', 'r') as f:
    data = f.read()

wlist = data.split('\n')

flist = glob.glob('evidence/e1/ev_log/**')

for f in flist:
    with open(f, 'r') as f:
        for w in wlist:
            print(f.name, w)
            data = f.read()
            m = re.search(data, w)
            if m is not None:
                print('exist {}'.format(m.group()))
