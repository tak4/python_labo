import requests

url = "https://requests.readthedocs.io/en/latest/"
response = requests.get(url)

print(type(response))

# print(response.text)