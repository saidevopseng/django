import requests
BASE_URL='http://127.0.0.1:8000/'
ENDPOINT='apijson'
resp=requests.get(BASE_URL+ENDPOINT)
print(resp.json())
print(type(resp.json()))
print(type(resp))

data=resp.json()
print('Data from django app:')
print('_'*30)
print('Employee Number:',data['eno'])
print('Employee Name:',data['ename'])
print('Employee Salary:',data['esal'])
print('Employee Address:',data['eaddr'])