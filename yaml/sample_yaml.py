import yaml

with open('config.yaml', 'r') as file:
    config = yaml.load(file)

for k, v in config.items():
    for k2, v2 in config[k].items():
        print(k2, v2)