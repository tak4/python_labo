import os
import pprint
import sys
import json

KEY_SUMMARY         = 'summary'
KEY_PARAMETERS      = 'parameters'
KEY_REQUEST_BODY    = 'requestBody'

KEY_APPLICATION_JSON        = 'application/json'
KEY_MILTIPART_FORM_DATA     = 'multipart/form-data'


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
        print(data_path[rm][KEY_SUMMARY])

        # parameters
        if KEY_PARAMETERS in data_path[rm]:
            parameters = data_path[rm][KEY_PARAMETERS]
            print(KEY_PARAMETERS)
            for param in parameters:
                # print(param['name'])
                pprint.pprint(param)

        # requestBody
        if KEY_REQUEST_BODY in data_path[rm]:
            request_body_content = data_path[rm][KEY_REQUEST_BODY]['content']
            print(KEY_REQUEST_BODY)
            if KEY_APPLICATION_JSON in request_body_content:
                # print(request_body_content[KEY_APPLICATION_JSON]['schema'])
                # pprint.pprint(request_body_content[KEY_APPLICATION_JSON]['schema'])
                if '$ref' in request_body_content[KEY_APPLICATION_JSON]['schema']:
                    ref = request_body_content[KEY_APPLICATION_JSON]['schema']['$ref']
                    ref_list = ref.split('/')
                    data_contents = data[ref_list[1]][ref_list[2]][ref_list[3]]
                    pprint.pprint(data_contents)
            if KEY_MILTIPART_FORM_DATA in request_body_content:
                # print(request_body_content[KEY_MILTIPART_FORM_DATA]['schema'])
                # pprint.pprint(request_body_content[KEY_MILTIPART_FORM_DATA]['schema'])
                if '$ref' in request_body_content[KEY_MILTIPART_FORM_DATA]['schema']:
                    ref = request_body_content[KEY_MILTIPART_FORM_DATA]['schema']['$ref']
                    ref_list = ref.split('/')
                    data_contents = data[ref_list[1]][ref_list[2]][ref_list[3]]
                    pprint.pprint(data_contents)
