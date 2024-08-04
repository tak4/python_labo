import urllib.request
import json

print('--- GET ---')
url = 'http://httpbin.org/get'
print('-> response')
with urllib.request.urlopen(url) as f:
    print(json.loads(f.read().decode('utf-8')))

print('--- GET + query param ---')
payload = {'key1': 'value1', 'key2': 'value2'}
url = 'http://httpbin.org/get' + '?' + urllib.parse.urlencode(payload)
print(url)
print('-> response')
with urllib.request.urlopen(url) as f:
    print(json.loads(f.read().decode('utf-8')))

print('--- POST ---')
req = urllib.request.Request('http://httpbin.org/post')
# payloadを文字列(json)にして、UTF-8でエンコード
payload = json.dumps(payload).encode('utf-8')
req = urllib.request.Request(
    'http://httpbin.org/post', data=payload, method='POST'
)
print('-> response')
with urllib.request.urlopen(req) as f:
    print(json.loads(f.read().decode('utf-8')))

print('--- PUT ---')
req = urllib.request.Request(
    'http://httpbin.org/put', data=payload, method='PUT'
)
print('-> response')
with urllib.request.urlopen(req) as f:
    print(json.loads(f.read().decode('utf-8')))

print('--- DELETE ---')
req = urllib.request.Request(
    'http://httpbin.org/delete', data=payload, method='DELETE'
)
print('-> response')
with urllib.request.urlopen(req) as f:
    print(json.loads(f.read().decode('utf-8')))