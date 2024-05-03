import json

with open('data.json', 'r') as f:
    data = json.load(f)

print(data)
print(type(data))
print(data['project_id'])

with open('data2.json', 'w') as file:
    json.dump(data, file, indent=6)

json_string = '{"name": "John", "age": 30, "city": "New York"}'
json_dict = {"name": "John", "age": 30, "city": "New York"}

data = json.loads(json_string)

print(data)

print(json.dumps(json_dict, indent=2))

# Working on Errors
json_string = '{"name": "John", "age": 30, "city": "New York"'

try:
    data = json.loads(json_string)
    print(data)
except json.JSONDecodeError as e:
    print('Error during json deserialization:', e)

try:
    with open('data3.json', 'w') as file:
        json.dump(data, file)
        print("Дані записані у файл")
except PermissionError as e:
    print("Немає прав доступу до файлу", e)

try:
    with open('data4.json', 'r') as file:
        data = json.load(file)
        print(data)
except FileNotFoundError as e:
    print("Файл не знайдено", e)
