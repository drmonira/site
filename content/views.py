from django.shortcuts import render,redirect
from django.http.response import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='/logreg/') 
def content_view(request):
    return render(request,"lsssons-gal.html",{"token":1,"username":request.user.username})


    
@login_required(login_url='/logreg/')    
def content_etails_view(request):
    return render(request,"lsssons-gal.html",{"token":1,"username":request.user.username})
def content_details_view(request,lesson_id):
    lessonurl='lessons/'
    if lesson_id==str(1):
        lessonurl+="1t.html"
    elif lesson_id==str(2):
        lessonurl+="2t.html"
    elif lesson_id==str(3):
        lessonurl+="3t.html"
    elif lesson_id==str(4):
        lessonurl+="4t.html"
    elif lesson_id==str(5):
        lessonurl+="5t.html"
    elif lesson_id==str(6):
        lessonurl+="6t.html"
    elif lesson_id==str(7):
        lessonurl+="7t.html"
    elif lesson_id==str(8):
        lessonurl+="8t.html"
    elif lesson_id==str(9):
        lessonurl+="9t.html"
    elif lesson_id==str(10):
        lessonurl+="10t.html"
    else:
        return HttpResponse("<h1> lesson is not here : "+str(lesson_id)+"</h1>")
        lessonurl+="10.html"
    return render(request,lessonurl,{"token":1,"username":request.user.username})

def contentnew_view(request):
    return render(request, "newgal.html")