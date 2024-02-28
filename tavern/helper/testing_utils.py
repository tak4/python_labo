import json

def is_specified_json(response, schema):
    json = response.json()
    assert json.get("item") == schema.get("item")

def save_response(response):
    j = response.json()
    with open("data.json", "w") as f:
        # JSONデータを書き出す
        json.dump(j, f)
