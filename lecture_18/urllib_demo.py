import json
import urllib.request
import urllib.parse



# urllib.request

# GET
url = 'https://fakerestapi.azurewebsites.net/api/v1/Activities'
response = urllib.request.urlopen(url)
data = response.read()

print(data)
print(type(data))
new_data = json.loads(data)
print(new_data)
print(type(new_data))
for item in new_data:
    print(type(item))
    print(item)

# POST
url = 'https://dummy.restapiexample.com/api/v1/create'
data = {'name': 'Yurii', 'salary': '1', 'age': '35'}
payload = urllib.parse.urlencode(data).encode()
req = urllib.request.Request(url=url, data=payload, method='POST')
req.add_header('User-Agent', 'PostmanRuntime/7.32.1')
response = urllib.request.urlopen(req)
result = response.read()
print(result)



# urllib.parse

# urllib.error

