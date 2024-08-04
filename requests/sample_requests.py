import requests

payload = {'key1': 'value1', 'key2': 'value2'}

# GET
r = requests.get('http://httpbin.org/get', params=payload, timeout=1)
print('--- GET ---')
print(r.status_code)
print(r.text)
print(r.json())

# POST
r = requests.post('http://httpbin.org/post', data=payload)
print('--- POST ---')
print(r.status_code)
print(r.text)
print(r.json())

# PUT
r = requests.put('http://httpbin.org/put', data=payload)
print('--- PUT ---')
print(r.status_code)
print(r.text)
print(r.json())

# DELETE
r = requests.delete('http://httpbin.org/delete', data=payload)
print('--- DELETE ---')
print(r.status_code)
print(r.text)
print(r.json())


