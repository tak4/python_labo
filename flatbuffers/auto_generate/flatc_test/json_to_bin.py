import base64
import json
import os
import sys

def main():
    if len(sys.argv) <= 1:
        print('Error!!!')
        return

    json_file_name = sys.argv[1]
    print(sys.argv[1])

    with open(json_file_name, 'r') as f:
        json_data = json.load(f)

    b64data = json_data['properties']['O']

    bdata = base64.b64decode(b64data)
    bin_filename = os.path.basename(json_file_name).split('.')[0] + '.bin'
    with open(bin_filename, 'wb') as f:
        f.write(bdata)

if __name__ == '__main__':
    main()
