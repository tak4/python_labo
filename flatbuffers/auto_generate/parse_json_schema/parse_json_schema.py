import json
import os
import pprint
import sys
base_path = os.path.dirname(
                    os.path.dirname(
                        os.path.abspath(__file__)))
sys.path.append(base_path)
from SmartCamera import BoundingBox
from SmartCamera import BoundingBox2d
from SmartCamera import ObjectDetectionTop
import SmartCamera


with open('../json/jsonschema/objectdetection.schema.json', 'r') as f:
    json_schema = json.load(f)

# pprint.pprint(json_schema, indent=2)

for k, v in json_schema['definitions'].items():
    definition = k.split('_')
    print(definition[-1])
    if 'type' in v:
        type = v['type']
        print(type)

    if 'properties' in v:
        for property, property_v in v['properties'].items():
            print(property)
            if 'type' in property_v:
                property_type = property_v['type']
                print(property_type)


