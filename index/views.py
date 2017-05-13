from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.
def index_view (request):
    return HttpResponse("<h1> the main page </h1>")