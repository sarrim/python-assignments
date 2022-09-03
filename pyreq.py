import requests

res = requests.get('https://reqres.in/api/users?page=2')

print(res.status_code)