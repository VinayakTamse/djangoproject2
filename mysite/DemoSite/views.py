from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse
from django.views import View
from .models import DemoSite, DemoUser

# Create your views here.

class IndexPage(View):
    def get(self, request):
        return render(request, 'DemoSite/index.html')

    def post(self, request):
        name = request.POST['name']
        lname = request.POST['lname']
        email = request.POST['email']
        image = request.POST['Img']
        gender = request.POST['gender']
        hobbies = request.POST['hobbies']
        dem = DemoSite(name=name, email=email, photo=image, gender=gender, hobbies=hobbies)
        dem.save()
        return redirect('/')

def CreateOperation(request):

    if request.method == 'POST':
        id = request.POST.get('u_id')
        name = request.POST.get('name')
        dept = request.POST.get('dept')
        age = request.POST.get('age')
        if id == '':
            dem_usr = DemoUser.objects.create(name=name, department=dept, age=age)
            dem_usr.save()

        else:
            dem_usr = DemoUser.objects.filter(id=id).update(name=name, department=dept, age=age)
        
        demo_users = DemoUser.objects.values()
        demo_users_lists = list(demo_users)
        return JsonResponse({'statusCode':201, 'response':'OK', 'demo_users_lists':demo_users_lists})


        
    demo_users = DemoUser.objects.all()
    parameters = {'demo_users':demo_users}
    
  

    return render(request, 'DemoSite/crudop.html', parameters)

def DeleteOperations(request):
    if request.method == 'POST':
        dem_id = request.POST.get('sid')
        #print("Value is",dem_id)
        del_id = DemoUser.objects.get(pk=dem_id)
        del_id.delete()
        return JsonResponse({'statusCode':200})


def UpdateOperations(request):
    if request.method == 'POST':
        dem_id = request.POST.get('sid')
        st_data = DemoUser.objects.get(pk=dem_id)
        js_data = {'id':st_data.id, 'name':st_data.name, 'department':st_data.department, 'age':st_data.age}
        return JsonResponse(js_data)




    






