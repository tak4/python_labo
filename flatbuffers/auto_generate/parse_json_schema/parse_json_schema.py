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
        schema schema
        definitions definitions以下の要素
    '''

    if isinstance(schema, dict):
        if '$ref' in schema:
            ref_path = schema['$ref'].split('/')
            ref_key = ref_path[-1]
            return {ref_key: resolve_refs(definitions[ref_key], definitions)}
        else:
            return {k: resolve_refs(v, definitions) for k, v in schema.items()}
    elif isinstance(schema, list):
        return [resolve_refs(item, definitions) for item in schema]
    else:
        # 末端の要素
        return schema

resolved_schema = resolve_refs(json_schema, json_schema.get('definitions', {}))

with open('output.yaml', 'w') as yaml_file:
    yaml.dump(resolved_schema, yaml_file, default_flow_style=False, allow_unicode=True)


def recursive(schema):
    if isinstance(schema, dict):
        for k, v in schema.items():
            if 'properties' == k:
                pass
            elif 'items' == v:
                print(f'{k}(list)')
            else:
                print(k)
            recursive(v)

recursive(resolved_schema)
