from django.shortcuts import render
from api2.models import Employee
from api2.serializers import EmployeeSerializer
from rest_framework import viewsets

# Create your views here.

class EmployeeAPI(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer