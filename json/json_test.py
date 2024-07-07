import json

# creating a dictionary
country_capitals = {
  "Germany": "Berlin", 
  "Canada": "Ottawa", 
  "England": "London",
  "Japan" : {"Tokyo": 2194}
}

# dictionay to json file
with open('./output/country_capitals.json', 'w') as f:
    json.dump(country_capitals, f, indent=4)

# dictionay to json string
s = json.dumps(country_capitals, indent=4)
print(s, type(s))

# with open('./output/country_capitals_shape.json', 'w') as f:
#     print(country_capitals)

# json.load() と json.loads() は、どちらも JSON 形式のデータを Python オブジェクトに変換する関数
# json.load() は、ファイルオブジェクトを引数として取る
with open('./output/country_capitals.json', 'r') as f:
    data = json.load(f)

# Pythonオブジェクトを出力
print(data)

# json.loads() は、文字列を引数として取る
data = json.loads(s)
print(s)

