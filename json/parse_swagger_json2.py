import json
import pprint

# Function to expand the $ref parts in the JSON data
def expand_refs(data, components):
    if isinstance(data, dict):
        if "$ref" in data:
            ref = data["$ref"]
            parts = ref.split('/')
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
with open('input/1_8_1_swagger.json', 'r') as f:
    before = json.load(f)

# Extract components
components = before.get("components", {})

j = expand_refs(before, components)

print(json.dumps(j, indent=2))
