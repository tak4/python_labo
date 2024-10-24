import os
import pprint
import sys
import json

KEY_SUMMARY = 'summary'
KEY_DESCRIPTION = 'description'
KEY_TAGS = 'tags'
KEY_OPERATIONID = 'operationId'
KEY_PARAMETERS = 'parameters'
KEY_REQUEST_BODY = 'requestBody'
KEY_RESPOMSES = 'responses'

KEY_APPLICATION_JSON = 'application/json'
KEY_MILTIPART_FORM_DATA = 'multipart/form-data'

target_summary = ''


nest_count = 0
def recursive_ref(nc, data, d):
    if isinstance(d, dict):
        for k, v in d.items():
            if '$ref' == k:
                ref_list = v.split('/')
                data_contents = data[ref_list[1]][ref_list[2]][ref_list[3]]
                recursive_ref(nc + 1, data, data_contents)
            else:
                # print('    ' * nc + '{:<15}: {}'.format(k, v))
                print('\t' * nc + f'{k}')
                recursive_ref(nc + 1, data, v)
    else:
        print('\t' * nc + f'{d}')

def main():

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

    set_req_method_keys = set()

    # pathsの中身を取得
    for path in data_paths_keys:

        data_path = data_paths[path]
        req_methods = data_path.keys()

        # method get/put/delete 等でまわす
        for rm in req_methods:
            summary = data_path[rm][KEY_SUMMARY]
            if target_summary == '' or summary == target_summary:
                print(f'# {summary}')
                print('----- path')
                print(path)
                print('----- method')
                print(f'{rm}')

                # keyの種類チェック用
                # for k in data_path[rm].keys():
                #     set_req_method_keys.add(k)

                # description
                if KEY_DESCRIPTION in data_path[rm]:
                    desctiption = data_path[rm][KEY_DESCRIPTION]
                    print(f'----- {KEY_DESCRIPTION}')
                    print(desctiption)

                # keys
                if KEY_TAGS in data_path[rm]:
                    tags = data_path[rm][KEY_TAGS]
                    print(f'----- {KEY_TAGS}')
                    print(tags)

                # operationid
                if KEY_OPERATIONID in data_path[rm]:
                    opeid = data_path[rm][KEY_OPERATIONID]
                    print(f'----- {KEY_OPERATIONID}')
                    print(opeid)

                # parameters
                if KEY_PARAMETERS in data_path[rm]:
                    parameters = data_path[rm][KEY_PARAMETERS]
                    print(f'----- {KEY_PARAMETERS}')
                    for params in parameters:
                        print('{}\t {}'.format('in', params['in']))
                        print('{}\t {}'.format('name', params['name']))
                        for k, v in params.items():
                            if k != 'in' and k != 'name':
                                print('{}\t {}'.format(k, v))

                # requestBody
                if KEY_REQUEST_BODY in data_path[rm]:
                    responses = data_path[rm][KEY_REQUEST_BODY]['content']
                    print(f'----- {KEY_REQUEST_BODY}')
                    recursive_ref(0, data, responses)
                    # for response in responses.keys():
                    #     print(response)
                        # if '$ref' in responses[response]['schema']:
                        #     ref = responses[response]['schema']['$ref']
                        #     ref_list = ref.split('/')
                        #     data_contents = data[ref_list[1]][ref_list[2]][ref_list[3]]
                        #     for k, v in data_contents.items():
                        #         print('{:<15}: {}'.format(k, v))


                # responses
                if KEY_RESPOMSES in data_path[rm]:
                    responses = data_path[rm][KEY_RESPOMSES]
                    print(f'----- {KEY_RESPOMSES}')
                    recursive_ref(0, data, responses)
                    # for response in responses:
                    #     pprint.pprint(responses[response])

                print()


    # keyの種類チェック用
    for s in set_req_method_keys:
        print(s)


if __name__ == '__main__':
    main()
