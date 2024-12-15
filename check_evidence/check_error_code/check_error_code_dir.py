import glob
import os
import re
import sys

if len(sys.argv) <= 1:
    print('no input file...')
    sys.exit()

input_path = sys.argv[1]
target_path = os.path.join(input_path, '**')
file_path_list = glob.glob(target_path)

with open('error_code_list.txt', 'r') as f:
    data = f.read()
wlist = data.split('\n')

for file_path in file_path_list:
    if os.path.isfile(file_path):
        with open(file_path, 'r') as f:
            data = f.read()
            for w in wlist:
                print(f.name, w)
                m = re.findall(w, data)
                for w in m:
                    print('exist {}'.format(w))
