import base64
import os
import sys
import string

json_template = '''{
    "properties": {
        "O": "$b64data"
    }
}
'''


def main():
    if len(sys.argv) <= 1:
        print('Error!!!')
        return

    bin_file_name = sys.argv[1]
    print(sys.argv[1])

    with open(bin_file_name, 'rb') as f:
        bin_data = f.read()
        base64_data = base64.b64encode(bin_data)

    t = string.Template(json_template)
    json_output = t.substitute(b64data=base64_data.decode())
    print(json_output)

    json_filename = os.path.basename(bin_file_name).split('.')[0] + '.json'
    with open(json_filename, 'w') as f:
        f.write(json_output)

if __name__ == '__main__':
    main()
