import requests

r = requests.get('http://localhost:5000/techtalk')

print(r.text)

payload = { "message": "Hello there!" }
header = { 'Content-Type': 'application/json' }

x = requests.post('http://localhost:5000/ilikecs', json = payload, headers = header)

print(x.json())
