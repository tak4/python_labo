def is_specified_json(response, schema):
    json = response.json()
    assert json.get("item") == schema.get("item")
