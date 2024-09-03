import os

def convert_crlf_to_lf(directory):
    for foldername, subfolders, filenames in os.walk(directory):
        for filename in filenames:
            if filename.endswith('.txt'):
                filepath = os.path.join(foldername, filename)
                with open(filepath, 'r', encoding='utf-8') as file:
                    content = file.read()
                content = content.replace('\r\n', '\n')
                with open(filepath, 'w', encoding='utf-8') as file:
                    file.write(content)

def convert_lf_to_crlf(directory):
    for foldername, subfolders, filenames in os.walk(directory):
        for filename in filenames:
            if filename.endswith('.txt'):
                filepath = os.path.join(foldername, filename)
                with open(filepath, 'r', encoding='utf-8') as file:
                    content = file.read()
                content = content.replace('\n', '\r\n')
                with open(filepath, 'w', encoding='utf-8') as file:
                    file.write(content)

convert_crlf_to_lf('target')
# convert_lf_to_crlf('target')
