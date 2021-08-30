from django.http.response import Http404, HttpResponseForbidden, HttpResponseNotFound
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import AgentMode, ExtraField, Member, UserMember
import re
from .forms import UsersMemberRegister, Agents
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django import views
from blog.models import BlogPosts
from home.models import Profile
from home.forms import ProfileForm

# Create your views here.
@login_required(login_url='/login/')
def home(request):
    use = request.user.id
    um = UserMember.objects.filter(usermemberId = use)
    
    
        

    return render(request, 'home/home.html', {'datas':um})

def registerUser(request):

    if request.method == 'POST':

        Username = request.POST['uname']
        Email = request.POST['email']
        Password1 = request.POST['pass1']
        Password2 = request.POST['pass2']
        Phone = request.POST['phone']
        gender = request.POST['exampleRadios']

        user_regex = '^[A-Z][a-z]{4,12}$'
        email_regex = '[A-Za-z0-9.]+[@][A-Za-z0-9]+(.com|.in)'
        password_regex = '[A-Za-z]+[0-9]+[%$#@!*]+{5,12}'

        validate_user = re.search(user_regex, Username)
        validate_email = re.search(email_regex, Email)
        if validate_user is None:
            messages.error(request, 'Invalid User Name')
            return redirect('/register')
        elif validate_email is None:
            messages.error(request, 'Invalid email id')
            return redirect('/register')


        else:

            newUser = User.objects.create_user(username=Username, email=Email, password=Password1)
            extras = ExtraField(phone_no=Phone, gender=gender, user = newUser)
            extras.save()
            newUser.save()
            messages.success(request, 'User Created')
            return redirect('/')

        

    return render(request, 'home/register.html')

def hadleLogin(request):

    if request.method == 'POST':

        UserName = request.POST['username']
        PassWord = request.POST['u_password']
        myUser = authenticate(username=UserName, password=PassWord)
    

        if myUser is not None:
            login(request, myUser)
            messages.success(request, 'Login is Success')
            return redirect('/')
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('/')

    return render(request, 'home/login.html')

def handleLogout(request):

    if request.method == 'POST':

        logout(request)
        return render(request, 'home/logout.html')

    return HttpResponse('<div style="text-align:center;"><svg viewbox="0 0 50 50" height="200px" width="700px"><text x="-45" y="30" stroke="red">404 Page Not Found</text></svg></div>')


def members(request):
    try:

        if request.method == 'POST':
            username = request.POST.get('name')
            email = request.POST.get('email')
            phone = request.POST.get('number')

            mem = Member(name=username, email=email, phone=phone)
            mem.save()
            messages.success(request,'Added Member Successfully')
            
            return redirect('/members/')
    except Exception as e:

        return HttpResponseForbidden()
    memb = Member.objects.all()
   
    params = {'member':memb}

    return render(request, 'home/members.html', params)

def delete_members(request, user_id):

    if request.method == 'POST':
        mem = Member.objects.get(pk=user_id)
        mem.delete()
        messages.warning(request, 'Deleted Member')
        return redirect('/members/')

    return HttpResponseNotFound()

def Update_member(request, id):

    if request.method == 'POST':
        #pm = Member.objects.get(pk=id)
        lm = Member.objects.filter(id=id).update(name=request.POST.get('name'),email=request.POST.get('email'),phone=request.POST.get('number'))
        #pm.name = request.POST.get('name')
        #pm.email = request.POST.get('email')
        #pm.phone = request.POST.get('number')
        #up = Member(pm.id,pm.name, pm.email, pm.phone)
        #up.save()
        messages.success(request, 'Update Success')
        return redirect('/members/')


    pm = Member.objects.get(pk=id)
    return render(request, 'home/update.html', {'mem_id':pm})

def user_members_add(request, id):
    if request.method == 'POST':
        us = User.objects.get(id=id)
        umr = UsersMemberRegister(request.POST)
        if umr.is_valid():
            
            name = umr.cleaned_data['Name']
            email = umr.cleaned_data['Email']
            umem = UserMember(usermemberId=us,Name=name, Email=email)
            umem.save()
            return redirect('/')
    if request.user.is_authenticated:
        umr = UsersMemberRegister()

        return render(request, 'home/usermember.html', {'form':umr})
    else:
        return HttpResponse('<h1>Please Login</h1>')

def agents(request):
    if request.method == 'POST':
        ag = Agents(request.POST)
        if ag.is_valid():
            name = ag.cleaned_data['Agent_Name']
            phone = ag.cleaned_data['Agent_Phone']
            agm = AgentMode(ag_name=name, ag_phone=phone)
            agm.save()
            
            return redirect('/')

    ag = Agents()
    dis_ag = AgentMode.objects.all()

    return render(request, 'home/agent.html', {'form':ag, 'agents':dis_ag})

class SearchView(views.View):
    
    def get(self, request):
        
        if request.user.is_authenticated:
            query = request.GET['search']
            if len(query)>50:
                bp = BlogPosts.objects.none()

            bpt = BlogPosts.objects.filter(blog_title__icontains=query)
            bpc = BlogPosts.objects.filter(blog_content__icontains=query)
            bp = bpt.union(bpc)

            
            return render(request, 'home/search.html', {'search_post':bp,'query':query})
        else:
            return HttpResponse('<div style="text-align:center;"><svg viewbox="0 0 50 50" height="200px" width="700px"><text x="-45" y="30" stroke="red">404 Page Not Found</text></svg></div>')
        
class AddProfile(views.View):

    def get(self, request):

        prof_form = ProfileForm()
        send = {'form':prof_form}

        return render(request, 'home/profile.html', send)

    def post(self, request):
        profile_form = ProfileForm(request.POST, request.FILES)
        print(profile_form.errors)
        print(profile_form.is_valid())
        try:
            if profile_form.is_valid():
           
                profile_form.save()
                return redirect('/profile/')
            else:
                return HttpResponse('<h1>Validation Failed</h1>')
        except Exception as e:
            return HttpResponse(e)


