import requests,json,time
BASE_URL='http://127.0.0.1:8000/'
ENDPOINT='api/'

print('get request')
# def get_resource(id):
def get_resource(id=None):
    data={}
    if id is not None:
        data={
            'id':id
        }
    
    resp=requests.get(BASE_URL+ENDPOINT,data=json.dumps(data))
    print(resp.status_code)
    print(resp.json())
# get_resource() # will get all records
get_resource(11)
# get_resource()
time.sleep(10)

print('post request')
def create_resource():
    new_emp={
        'eno':102,
        'ename':'nanna',
        # 'esal':1000, #to check validation
        'esal':150000,
        'eaddr':'home',
    }
    # resp=requests.post(BASE_URL+ENDPOINT,data=new_emp) # used to check validation working or not?
    resp=requests.post(BASE_URL+ENDPOINT,data=json.dumps(new_emp))
    print(resp.status_code)
    print(resp.json())
create_resource()
time.sleep(15)

print('update request')
def update_resource(id=None):
    new_emp={
        'id':id,
        # 'eno':103,
        # 'ename':'chaitu',
        'ename':'amma',
        # 'ename':'amma aruna',
        # 'esal':250000,
        # 'esal':1000,
        'esal':200000,
        # 'esal':3000,
        'eaddr':'netherlands', 
    }

    resp=requests.put(BASE_URL+ENDPOINT,data=json.dumps(new_emp))
    print(resp.status_code)
    print(resp.json())

update_resource(11)
time.sleep(15)

print('delete request')
def delete_resource(id=None):
    data={
        'id':id
    }

    resp=requests.delete(BASE_URL+ENDPOINT,data=json.dumps(data))
    print(resp.status_code)
    print(resp.json())

delete_resource(11)
