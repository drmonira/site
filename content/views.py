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
        lessonurl+="1.html"
    elif lesson_id==str(2):
        lessonurl+="2.html"
    elif lesson_id==str(3):
        lessonurl+="3.html"
    elif lesson_id==str(4):
        lessonurl+="4.html"
    elif lesson_id==str(5):
        lessonurl+="5.html"
    elif lesson_id==str(6):
        lessonurl+="6.html"
    elif lesson_id==str(7):
        lessonurl+="7.html"
    elif lesson_id==str(8):
        lessonurl+="8.html"
    elif lesson_id==str(9):
        lessonurl+="9.html"
    elif lesson_id==str(10):
        lessonurl+="10.html"
    else:
        return HttpResponse("<h1> lesson is not here : "+str(lesson_id)+"</h1>")
        lessonurl+="10.html"
    return render(request,lessonurl,{"token":1,"username":request.user.username})
