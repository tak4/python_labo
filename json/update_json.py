import json
import pprint

# jsonファイルを辞書型で読み込み
with open('./input/tohoho_sample.json', 'r') as f:
    json_data = json.load(f)    # 辞書型を返す
print(type(json_data))
pprint.pprint(json_data)

print()
object_list = json_data['object_list']  # 参照取得
for l in object_list:
    l['age'] = 48   # 更新

print(object_list)

# 辞書型(更新済み)をjsonファイルに書き込み
with open('./output/update_sample.json', 'w') as f:
    json.dump(json_data, f, indent=4)

