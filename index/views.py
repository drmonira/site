from django.shortcuts import render,redirect
from django.http.response import HttpResponse

# Create your views here.
def index_view (request):
    if request.user.is_authenticated:
        token=True
        username=request.user.username
        return render (request,"index.html",{'token':token,'username':username})
    else:
        token=False
        return render (request,"index.html",{'token':token})
    

def log_reg(request):
    return render(request,"log_reg.html",{'next':request.GET['next']})
def content_view(request):
    return render(request,"lsssons-gal.html",{"token":1,"username":request.user.username})
def mainlogin_view(request):
    return redirect(index_view)
#@login_required(login_url='/logreg/')
#def mainlogin_view_admin(request):
#    return redirect("admin/")
def more_view(request):
    return  HttpResponse("<h1>more her<br>"+ request.path + "</h1>")