import json

def is_specified_json(response, schema):
    json = response.json()
    assert json.get("name") == schema.get("name")

def save_response(response, fname):
    j = response.json()
    with open(fname, "w") as f:
        # JSONデータを書き出す
        json.dump(j, f)
