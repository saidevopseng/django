from django.contrib import admin
from firstapp.models import Employee

# Register your models here
class EmployeeAdmin(admin.ModelAdmin):
    list_display=['pk','id','eno','ename','esal','eaddr']
admin.site.register(Employee,EmployeeAdmin)

