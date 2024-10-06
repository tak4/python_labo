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
        # keyがdictかlistでなく、末端の要素の場合は再帰せず、そのまま返す
        return schema

def get_object_value(schema, key):
    ret_value = None
    # object内を走査する
    if isinstance(schema, dict):
        for k, v in schema.items():
            if key == k:
                ret_value = v
                break
    return ret_value

def snake_to_camel(snake_str):
    components = snake_str.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])

stack = deque()
def recursive(schema = None, parent = None, indent = 0):
    if parent is not None:
        stack.append(parent)

    indent = len(stack)

    if isinstance(schema, dict):
        for k, v in schema.items():
            obj_type = get_object_value(schema[k], "type")
            if "object" == obj_type:
                if parent is None:
                    # root_typeの処理
                    module_names = k.split('_')
                    print(f'elem{indent} = ', end="")
                    print('.'.join(module_names[1:]) + '.', end="")
                    print(f'GetRootAs{module_names[-1]}(buf, 0)')
                obj_properties = get_object_value(schema[k], "properties")
                recursive(obj_properties, k, len(stack))
            if "array" == obj_type:
                obj_items = get_object_value(schema[k], "items")
                print('  ' * indent + f'elem{indent} = elem{indent-1}.{snake_to_camel(k)}()')
                recursive(obj_items, k, len(stack))
            elif "number" == obj_type or "string" == obj_type:
                print(k, v)
            elif obj_type == None:
                print('  ' * indent + f'elem{indent} = elem{indent-1}.{k.title()}()')
                recursive(v, k, len(stack))

            # if 'type' == k:
            #     print('  ' * indent + f'{stack[-1]} -> {k}: {v}')
            #     if indent > 0:
            #         print('  ' * indent + f'elem{indent} = elem{indent-1}.{stack[-1]}()')

            #     # ネストを1段下げて再帰
            #     stack.append(k)
            #     recursive(v, len(stack))
            #     stack.pop()
            # elif 'enum' == k:
            #     print('  ' * indent + f'{stack[-1]} -> {k}: {v}')
            # elif 'additionalProperties' == k:
            #     pass
            # elif 'properties' == k:
            #     recursive(v, len(stack))
            # else:
            #     if indent == 0:
            #         # root_typeの処理
            #         module_names = k.split('_')
            #         print(f'elem{indent} = ', end="")
            #         print('.'.join(module_names[1:]) + '.', end="")
            #         print(f'GetRootAs{module_names[-1]}(buf, 0)')
            #     # ネストを1段下げて再帰
            #     stack.append(k)
            #     recursive(v, len(stack))
            #     stack.pop()
    elif isinstance(schema, list):
        for l in schema:
            recursive(l, stack[-1], indent)
    if parent is not None:
        stack.pop()

resolved_schema = resolve_refs(json_schema, json_schema.get('definitions', {}))

with open('output.yaml', 'w') as yaml_file:
    yaml.dump(resolved_schema, yaml_file, default_flow_style=False, allow_unicode=True)

recursive(schema=resolved_schema, parent=None, indent=0)

print(stack)