# 読み込み safe_load()
from pprint import pprint
import yaml

with open('./config/config.yaml', 'r') as yaml_file:
    data = yaml.safe_load(yaml_file)
    # pprint(data['search_conditions'])
    for condition in data['search_conditions']:
        for file in condition['target_file']:
            print(file['file'])

