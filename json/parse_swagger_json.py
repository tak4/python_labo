import json
import os

def resolve_ref(obj, definitions, visited=None):
    if visited is None:
        visited = set()

    if isinstance(obj, dict):
        if '$ref' in obj:
            ref_path = obj['$ref'].split('/')
            ref = definitions
            for part in ref_path[1:]:
                ref = ref.get(part)
                if ref is None:
                    raise KeyError(f"Reference path {obj['$ref']} could not be resolved.")
            
            if id(ref) in visited:
                raise ValueError(f"Circular reference detected at {obj['$ref']}.")
            visited.add(id(ref))
            
            return resolve_ref(ref, definitions, visited)
        return {k: resolve_ref(v, definitions, visited) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [resolve_ref(item, definitions, visited) for item in obj]
    else:
        return obj

def expand_refs(json_data):
    if 'components' in json_data and 'schemas' in json_data['components']:
        definitions = json_data['components']['schemas']
        return resolve_ref(json_data, definitions)
    return json_data

# Replace 'swagger.json' with the path to your JSON file
with open('input/1_8_1_swagger.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

expanded_data = expand_refs(data)

# Save the expanded JSON to a new file
with open('expanded_swagger.json', 'w', encoding='utf-8') as file:
    json.dump(expanded_data, file, ensure_ascii=False, indent=2)
