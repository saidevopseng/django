from rest_framework.serializers import ModelSerializer
from firstapp.models import Employee

class EmployeeSerializer(ModelSerializer):
    class Meta:
        model=Employee
        fields='__all__'