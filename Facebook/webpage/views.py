from django.shortcuts import render,HttpResponse

# Create your views here.
def home(req):
    return HttpResponse("Hello")