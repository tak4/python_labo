import os
import json

SAVE_DIR = f"./save/"

def is_specified_json(response, schema):
    json = response.json()
    assert json.get("name") == schema.get("name")

def save_response(response, fname):
    j = response.json()

    if not os.path.isdir(SAVE_DIR):
        os.mkdir(SAVE_DIR)

    with open(SAVE_DIR + fname, "w") as f:
        # JSONデータを書き出す
        json.dump(j, f)

def disp_response(response, _id):

    if not os.path.isdir(SAVE_DIR):
        os.mkdir(SAVE_DIR)

    with open(f"./save/_id.txt", "w") as f:
        f.write(_id)