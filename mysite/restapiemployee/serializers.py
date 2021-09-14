from rest_framework import serializers
from .models import Employee, Student

class EmpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class StuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
