from collections import deque
import json
import os
import pprint
import sys
import yaml
base_path = os.path.dirname(
                    os.path.dirname(
                        os.path.abspath(__file__)))
sys.path.append(base_path)

with open('../json/jsonschema/objectdetection.schema.json', 'r') as f:
    json_schema = json.load(f)

# pprint.pprint(json_schema, indent=2)

def resolve_refs(schema, definitions):
    '''flatbuffrers jsonschemaのrefを解決して階層構造に展開する
    Args:
        schema : schema
        definitions : definitions以下の要素
    '''

    if isinstance(schema, dict):
        if '$ref' in schema:
            # keyが'$ref' の場合は子要素を探す
            ref_path = schema['$ref'].split('/')
            ref_key = ref_path[-1]
            return {ref_key: resolve_refs(definitions[ref_key], definitions)}
        else:
            # keyが'$ref'でなければdictを展開する
            return {k: resolve_refs(v, definitions) for k, v in schema.items()}
    elif isinstance(schema, list):
        # keyがlistであれば、listを展開する
        return [resolve_refs(item, definitions) for item in schema]
    else:
        # keyがdictかlistでなく、末端の要素の場合は再帰しない
        return schema

resolved_schema = resolve_refs(json_schema, json_schema.get('definitions', {}))

with open('output.yaml', 'w') as yaml_file:
    yaml.dump(resolved_schema, yaml_file, default_flow_style=False, allow_unicode=True)


stack = deque()

def recursive(schema, indent):
    if isinstance(schema, dict):
        for k, v in schema.items():
            
            if 'type' == k or 'enum' == k or 'additionalProperties' == k:
                print('  ' * indent + f'{k}: {v}')
            else:
                print('  ' * indent + k)
            # if 'properties' == k:
            #     pass
            # elif 'type' == k:
            #     print(f'{k}: {v}')
            # else:
            #     print(k)
            
            stack.append(k)
            recursive(v, len(stack))
            stack.pop()
    elif isinstance(schema, list):
        for l in schema:
            recursive(l, indent)



recursive(resolved_schema, 0)

print(stack)