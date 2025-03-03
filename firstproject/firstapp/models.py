from django.db import models

# Create your models here.
class CustomManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(esal__gte=180000)
    
class CustomManager2(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(esal__lte=120000)
    
class CustomManager3(models.Manager):
    def get_queryset(self):
        return super().get_queryset().order_by('eno')
    
class Employee(models.Model):
    eno=models.IntegerField()
    ename=models.CharField(max_length=30)
    esal=models.FloatField()
    eaddr=models.CharField(max_length=30)
    objects=CustomManager()

class ProxyEmployee(Employee):
    objects=CustomManager2()
    class Meta:
        proxy=True

class ProxyEmployee1(Employee):
    objects=CustomManager3()
    class Meta:
        proxy=True
