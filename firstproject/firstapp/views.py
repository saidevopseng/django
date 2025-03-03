from django.shortcuts import render
from firstapp.models import Employee,ProxyEmployee,ProxyEmployee1

# Create your views here
def display_view(request):
    # emp_list=Employee.objects.all()
    # emp_list=ProxyEmployee.objects.all()
    emp_list=ProxyEmployee1.objects.all()
    return render(request,'testapp/index.html',{'emp_list':emp_list})

