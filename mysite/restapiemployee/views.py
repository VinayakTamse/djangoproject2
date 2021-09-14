
from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Employee, Student
from .serializers import EmpSerializer, StuSerializer
from rest_framework import viewsets
from rest_framework.response import Response

# Create your views here.

class employee_lists_create(ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmpSerializer

class employee_ret_up_del(RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmpSerializer

class StudentAPI(viewsets.ViewSet):

    def list(self, request):
        stu_data = Student.objects.all()
        serilaize_data = StuSerializer(stu_data, many=True)
        return Response(serilaize_data.data)

    def retrieve(self, request, pk):
        stu_data = Student.objects.get(pk=pk)
        serialize_data = StuSerializer(stu_data)
        return Response(serialize_data.data)

    def update(self, request, pk):
        stu_data = Student.objects.get(pk=pk)
        serilaize_data = StuSerializer(stu_data, data=request.data)
        if serilaize_data.is_valid():
            serilaize_data.save()
            return Response({'msg':'Updated'})
        return Response(serilaize_data.errors)

    def partial_update(self, request, pk):
        stu_data = Student.objects.get(pk=pk)
        serilaize_data = StuSerializer(stu_data, data=request.data, partial=True)
        if serilaize_data.is_valid():
            serilaize_data.save()
            return Response({'msg':'Updated'})
        return Response(serilaize_data.errors)

    def create(self, request):
        stu_data = StuSerializer(data=request.data)
        if stu_data.is_valid():
            stu_data.save()
            return Response({'msg':'Created'})
        return Response(stu_data.errors)

    def destroy(self, request, pk):
        stu_instance = Student.objects.get(pk=pk)
        stu_instance.delete()
        return Response({'msg':'deleted'})

    
