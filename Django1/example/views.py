from django.shortcuts import render
from django.http import HttpResponse
from django import forms

def home(req):
    if req.method == 'POST':
        print("hello world")
        print(req.POST['user'])
    return render(req,"home.html") 
class UserForm(forms.Form):
    name = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())