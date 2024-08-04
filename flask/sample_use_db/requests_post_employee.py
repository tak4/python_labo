import requests

r = requests.get(
    'http://127.0.0.1:5000/employee/Alice'
)
print(r.text)

r = requests.post(
    'http://127.0.0.1:5000/employee', 
    data={'name': 'Alice'}
)
print(r.text)

r = requests.put(
    'http://127.0.0.1:5000/employee', 
    data={'name': 'Alice', 'new_name': 'Bob'}
)
print(r.text)

r = requests.delete(
    'http://127.0.0.1:5000/employee', 
    data={'name': 'Alice'}
)
print(r.text)

