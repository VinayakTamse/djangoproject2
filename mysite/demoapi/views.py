from functools import partial
from django.shortcuts import render
from rest_framework import decorators
from rest_framework.decorators import api_view
from rest_framework.response import Response
from demoapi.models import Employee, Material
from demoapi.serializers import EmployeeSerializer, MaterialSerializer
from rest_framework import status
from rest_framework.views import APIView

# Create your views here.

@api_view(['GET','POST','PUT','DELETE'])
def Employee_Data(request, id=None):
    if request.method == 'GET':
        if id is None:
            emp_data = Employee.objects.all()
            emp_data_serialize = EmployeeSerializer(emp_data, many=True)
            return Response(emp_data_serialize.data)
        emp_data = Employee.objects.get(pk=id)
        emp_data_serialize = EmployeeSerializer(emp_data)
        return Response(emp_data_serialize.data)

    if request.method == 'POST':
        serialize_data = EmployeeSerializer(data = request.data)
        if serialize_data.is_valid():
            serialize_data.save()
            return Response({'msg':'Created'}, status=status.HTTP_201_CREATED)
        return Response({'msg':'failed'}, status = status.HTTP_406_NOT_ACCEPTABLE)

    if request.method == 'PUT':
        if id is not None:
            employee_data = Employee.objects.get(pk=id)
            serialize_data = EmployeeSerializer(employee_data, data=request.data, partial=True)
            if serialize_data.is_valid():
                serialize_data.save()
                return Response({'msg':'data updated'}, status=status.HTTP_202_ACCEPTED)
            return Response({'msg':'Failed'}, status=status.HTTP_406_NOT_ACCEPTABLE)

    if request.method == 'DELETE':
        if id is not None:
            employee_data = Employee.objects.get(pk=id)
            employee_data.delete()
            return Response({'msg':'deleted'})

class Material_API(APIView):

    def get(self, request, id=None, format=None):

         ob = Material.objects.filter(pk=id)

         if ob==True:
        
            if id is not None:

                material_details = Material.objects.get(pk=id)
                mat_serializer = MaterialSerializer(material_details)
                return Response(mat_serializer.data)
            else:
                material_details = Material.objects.all()
                mat_serializer = MaterialSerializer(material_details, many=True)
                return Response(mat_serializer.data)
         else:

             return Response({'msg':'no content'}, status=status.HTTP_204_NO_CONTENT)


    def post(self, request, format=None):

        material_data = MaterialSerializer(data=request.data)
        if material_data.is_valid():
            material_data.save()
            return Response({'msg':'data created'}, status=status.HTTP_201_CREATED)
        return Response(material_data.errors)

    def put(self, request, id, format=None):
        mat_data = Material.objects.get(pk=id)
        mat_serializer = MaterialSerializer(mat_data, data=request.data, partial=True)
        if mat_serializer.is_valid():
            mat_serializer.save()
            return Response({'msg':'updated'}, status=status.HTTP_202_ACCEPTED)
        return Response(mat_serializer.errors)



    def delete(self, request, id):
        inst = Material.objects.get(pk=id)
        inst.delete()
        return Response({'msg':'Deleted'})
       
           
        
            



    