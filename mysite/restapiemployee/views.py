from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Employee
from .serializers import EmpSerializer

# Create your views here.

class employee_lists_create(ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmpSerializer

class employee_ret_up_del(RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmpSerializer
