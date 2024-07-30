import json

# creating a dictionary
country_capitals = {
  "Germany": "Berlin", 
  "Canada": "Ottawa", 
  "England": "London",
  "Japan" : {"Tokyo": 2194}
}

# dictionary
print('--- dictionary ---')
print(country_capitals, type(country_capitals))

# dictionay to string
s = json.dumps(country_capitals, indent=4)
print('--- dictionay to json string ---')
print(s, type(s))

# string to dictionary
# json.loads() は、文字列を引数として取る
data = json.loads(s)
print('--- string to dictionary ---')
print(data, type(data))


# dictionary to file(file)
print('--- dictionary to file(file) ---')
with open('./output/country_capitals.json', 'w') as f:
    json.dump(country_capitals, f, indent=4)

# with open('./output/country_capitals_shape.json', 'w') as f:
#     print(country_capitals)

# file(json) to dictionary
# json.load() は、ファイルオブジェクトを引数として取る
with open('./output/country_capitals.json', 'r') as f:
    data = json.load(f)
print('--- file(file) to dictionary ---')
print(data, type(data))

