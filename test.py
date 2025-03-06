import requests
r=requests.get('https://jsonplaceholder.typicode.com/todos/1')
data=r.json()
# print(type(data))
# print(data['title'])
# print(data['id'])
