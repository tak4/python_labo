import json
import os
import sys

if len(sys.argv) <= 1:
    print('need input file')
    sys.exit()

input_swagger_json_file = sys.argv[1]

# Function to expand the $ref parts in the JSON data
def expand_refs(data, components):
    if isinstance(data, dict):
        if "$ref" in data:
            ref = data["$ref"]
            parts = ref.split('/')
            # $refを差し替える
            data[parts[3]] = components[parts[2]][parts[3]]
            del data["$ref"]
            return data
        else:
            return {k: expand_refs(v, components) for k, v in data.items()}
    elif isinstance(data, list):
        return [expand_refs(item, components) for item in data]
    else:
        return data

# Read the before JSON data from a file
with open(input_swagger_json_file, 'r') as f:
    input_json = json.load(f)

# components部分を取得
components = input_json.get("components", {})

# refを展開する
j = expand_refs(input_json, components)

output_filename = os.path.basename(input_swagger_json_file)

output_swagger_json_file = 'expand_' + output_filename
with open(output_swagger_json_file, 'w') as f:
    json.dump(j, f, indent=2)

# print(json.dumps(j, indent=2))
