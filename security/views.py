from django.shortcuts import render,redirect
from django.http.response import HttpResponse
from django.contrib.auth.decorators import login_required
from index.views import index_view
from django.contrib.auth import authenticate, login ,logout
from django.contrib.auth.models import User
# Create your views here.

def log_reg(request):
    return render(request,"log_reg.html",{'next':request.GET['next']})

def user_auth_view(request):
    user=authenticate(username=request.POST["username"],password=request.POST["password"])
    if user is not None:
        login(request,user)
        page=request.POST["next"]
        if page=="/main/":
            return redirect(index_view)
        else:
            return redirect(page)
        
    else:
        return render(request,"login_error.html")
    
def user_reg_view(request):
    User.objects.create_user(request.POST["usernamesignup"],request.POST["emailsignup"],request.POST["passwordsignup"])
    #user = User.objects.create_user('john2', 'lennon@thebeatle4s.com', 'johnpassword')
    #user.save()
    user=authenticate(username=request.POST["usernamesignup"],password=request.POST["passwordsignup"])
    if user is not None:
        if user.is_active:
            login(request,user)
            page=request.POST["next"]
            if page=="/main/":
                return redirect(index_view)
            else:
                return redirect(page)
        
    else:
        return render(request,'main_page.html',{'token':False})
    
    
    
def logout_view(request):
    logout(request)
    return redirect(index_view)




@login_required(login_url='/logreg/')
def mainlogin_view(request):
    return redirect(index_view)