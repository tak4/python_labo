import os
import pprint
import sys
import json

KEY_SUMMARY = 'summary'
KEY_PARAMETERS = 'parameters'
KEY_REQUEST_BODY = 'requestBody'
KEY_RESPOMSES = 'responses'

KEY_APPLICATION_JSON = 'application/json'
KEY_MILTIPART_FORM_DATA = 'multipart/form-data'

target_summary = ''

# ファイル名取得
args = sys.argv
if 1 == len(args):
    print("Usage " + args[0] + " swagger.json")
    sys.exit()

# jsonファイル読み込み
json_file_name = sys.argv[1]
with open(json_file_name, 'r') as f:
    data = json.load(f)

# paths を取得
data_paths = data['paths']
data_paths_keys = data_paths.keys()

# pathsの中身を取得
for path in data_paths_keys:

    data_path = data_paths[path]
    req_methods = data_path.keys()

    # method get/put/delete 等でまわす
    for rm in req_methods:
        summary = data_path[rm][KEY_SUMMARY]
        if target_summary == '' or summary == target_summary:
            print(f'##### {summary}')

            # parameters
            if KEY_PARAMETERS in data_path[rm]:
                parameters = data_path[rm][KEY_PARAMETERS]
                print(f'----- {KEY_PARAMETERS}')
                for param in parameters:
                    pprint.pprint(param)

            # requestBody
            if KEY_REQUEST_BODY in data_path[rm]:
                responses = data_path[rm][KEY_REQUEST_BODY]['content']
                print(f'----- {KEY_REQUEST_BODY}')
                for response in responses.keys():
                    print(response)
                    if '$ref' in responses[response]['schema']:
                        ref = responses[response]['schema']['$ref']
                        ref_list = ref.split('/')
                        data_contents = data[ref_list[1]][ref_list[2]][ref_list[3]]
                        pprint.pprint(data_contents)

            # responses
            if KEY_RESPOMSES in data_path[rm]:
                responses = data_path[rm][KEY_RESPOMSES]
                print(f'----- {KEY_RESPOMSES}')
                for response in responses:
                    pprint.pprint(responses[response])

            print()