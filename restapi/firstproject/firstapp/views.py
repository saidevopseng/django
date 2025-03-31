from django.shortcuts import render 
from rest_framework import viewsets
from firstapp.models import Employee
from firstapp.serializers import EmployeeSerializer
from rest_framework.authentication import BasicAuthentication,SessionAuthentication
from rest_framework.permissions import IsAuthenticated

# create your views here
class EmployeeCrudCBV(viewsets.ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
    # authentication_classes=[BasicAuthentication]
    authentication_classes=[SessionAuthentication]
    permission_classes=[IsAuthenticated]