import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','firstproject.settings')
import django
django.setup()

from firstapp.models import Employee
from faker import Faker
from random import *

fake=Faker()
def phonenumbergen():
    d1=randint(6,9)
    num=''+str(d1)
    for i in range(9):
        num+=str(randint(0,9))
    return int(num)

def populate(n):
    for i in range(n):
        feno=randint(1001,9999)
        fename=fake.name()
        fesal=randint(100000,200000)
        feaddr=fake.city()
        emp_record=Employee.objects.get_or_create(
            eno=feno,
            ename=fename,
            esal=fesal,
            eaddr=feaddr)
n=int(input('Enter number of records:'))
populate(n)
print(f'{n} records inserted successfully...')
