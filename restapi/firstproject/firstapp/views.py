from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def emp_data_view(request):
    emp_data={
        'eno':101,
        'ename':'charan',
        'esal':77000,
        'eaddr':'Mumbai'
    }

    # resp='Employee Number:{}Employee Name:{}Employee Salary:{}Employee Address:{}'.format(emp_data['eno'],emp_data['ename'],emp_data['esal'],emp_data['eaddr'])
    
    # resp = '<h1>Employee Number: {} Employee Name: {} Employee Salary: {} Employee Address: {}</h1>'.format(
    # emp_data['eno'], emp_data['ename'], emp_data['esal'], emp_data['eaddr'])

    resp = '<h1>Employee Details</h1><p>Employee Number: {}<br>Employee Name: {}<br>Employee Salary: {}<br>Employee Address: {}</p>'.format(
    emp_data['eno'], emp_data['ename'], emp_data['esal'], emp_data['eaddr'])

    
    return HttpResponse(resp)

import json
def emp_data_jsonview(request):
    emp_data={
        'eno':101,
        'ename':'charan',
        'esal':77000,
        'eaddr':'Mumbai'
    }
    json_data=json.dumps(emp_data)
    return HttpResponse(json_data,content_type='application/json')

from django.http import JsonResponse
def emp_data_jsonview2(request):
    emp_data={
        'eno':101,
        'ename':'charan',
        'esal':77000,
        'eaddr':'Mumbai'
    }
    return JsonResponse(emp_data)