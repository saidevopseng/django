from django.contrib import admin
from firstapp.models import Employee,ProxyEmployee,ProxyEmployee1

# Register your models here
class EmployeeAdmin(admin.ModelAdmin):
    list_display=['eno','ename','esal','eaddr']
admin.site.register(Employee,EmployeeAdmin)

class ProxyEmployeeAdmin(admin.ModelAdmin):
    list_display=['eno','ename','esal','eaddr']
admin.site.register(ProxyEmployee,ProxyEmployeeAdmin)

class ProxyEmployeeAdmin1(admin.ModelAdmin):
    list_display=['eno','ename','esal','eaddr']
admin.site.register(ProxyEmployee1,ProxyEmployeeAdmin1)