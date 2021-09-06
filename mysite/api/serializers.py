from rest_framework import serializers
from api.models import Employee

class EmployeeSerializers(serializers.Serializer):
    
    name = serializers.CharField(max_length=30)
    email = serializers.EmailField(max_length=100)
    salary = serializers.IntegerField()

    def create(self, validate_data):
        return Employee.objects.create(**validate_data)