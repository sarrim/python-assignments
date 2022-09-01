import json

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'
print(x)
y = json.loads(x)
print(y['name'])