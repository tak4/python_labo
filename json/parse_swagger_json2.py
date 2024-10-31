import json

# Function to expand the $ref parts in the JSON data
def expand_refs(data, components):
    if isinstance(data, dict):
        if "$ref" in data:
            ref = data["$ref"]
            parts = ref.split('/')
            ref_data = components
            for part in parts[1:]:
                ref_data = ref_data.get(part, {})
            return expand_refs(ref_data, components)
        else:
            return {k: expand_refs(v, components) for k, v in data.items()}
    elif isinstance(data, list):
        return [expand_refs(item, components) for item in data]
    else:
        return data

# Read the before JSON data from a file
with open('input/1_8_1_swagger_sample_before.json', 'r') as f:
    before = json.load(f)

# Extract components
components = before.get("components", {})

# Expand the $ref parts in the before JSON data
for path, path_item in before["paths"].items():
    for method, operation in path_item.items():
        if "requestBody" in operation:
            schema_ref = operation["requestBody"]["content"]["application/json"]["schema"]
            if "$ref" in schema_ref:
                ref_key = schema_ref["$ref"].split("/")[-1]
                operation["requestBody"]["content"]["application/json"]["schema"] = components["schemas"][ref_key]
        if "responses" in operation:
            for response_code, response in operation["responses"].items():
                if "content" in response:
                    schema_ref = response["content"]["application/json"]["schema"]
                    if "$ref" in schema_ref:
                        ref_key = schema_ref["$ref"].split("/")[-1]
                        response["content"]["application/json"]["schema"] = components["schemas"][ref_key]

# Print the after JSON data
print(json.dumps(before, indent=2, ensure_ascii=False))

