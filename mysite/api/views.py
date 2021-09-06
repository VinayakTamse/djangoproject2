from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from api.models import Employee
from api.serializers import EmployeeSerializers
from rest_framework.renderers import JSONRenderer
import io
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def display_all_employee_data(request):
    employee_data = Employee.objects.all()
    serialize_data = EmployeeSerializers(employee_data, many=True)
    json_data = JSONRenderer().render(serialize_data.data)
    return HttpResponse(json_data, content_type="application/json")

def display_single_employee(request, id):
    employee = Employee.objects.get(pk=id)
    serialize_data = EmployeeSerializers(employee)
    json_data = JSONRenderer().render(serialize_data.data)
    return HttpResponse(json_data, content_type="application/json")

@csrf_exempt
def create_employee_data(request):
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        py_data = JSONParser().parse(stream)
        serialize = EmployeeSerializers(data=py_data)
        if serialize.is_valid():
            serialize.save()
            message = {'status':'OK', 'response':201}
            json_msg = JSONRenderer().render(message)
            return HttpResponse(json_msg, content_type='application/json')
        return JsonResponse({'message':'failed', 'err':serialize.errors})