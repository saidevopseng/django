from django.shortcuts import render 
from firstapp.models import Employee
from rest_framework.viewsets import ModelViewSet
from firstapp.serializers import EmployeeSerializer
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser,IsAuthenticatedOrReadOnly,DjangoModelPermissions
from rest_framework.authentication import TokenAuthentication

# Create your views here.
class EmployeeCRUDCBV(ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
    authentication_classes=[TokenAuthentication]
    # permission_classes=[IsAuthenticated]
    # permission_classes=[AllowAny]
    # permission_classes=[IsAdminUser]
    # permission_classes=[IsAuthenticatedOrReadOnly]
    permission_classes=[DjangoModelPermissions]

