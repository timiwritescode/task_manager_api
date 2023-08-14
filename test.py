import requests

BASE = 'http://localhost:5000/api/'

response = requests.get(BASE + 'tasks/1?all=true')

print(response.json())