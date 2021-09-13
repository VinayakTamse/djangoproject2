from rest_framework import serializers
from demoapi.models import Employee, Material

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:

        model = Employee
        fields = ['emp_id', 'emp_name', 'emp_salary']

class MaterialSerializer(serializers.ModelSerializer):

    class Meta:

        model = Material
        fields = '__all__'