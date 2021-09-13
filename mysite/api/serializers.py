from rest_framework import serializers
from api.models import Employee

class EmployeeSerializers(serializers.Serializer):
    
    name = serializers.CharField(max_length=30)
    email = serializers.EmailField(max_length=100)
    salary = serializers.IntegerField()

    def create(self, validate_data):
        return Employee.objects.create(**validate_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.salary = validated_data.get('salary', instance.salary)
        instance.save()
        return instance