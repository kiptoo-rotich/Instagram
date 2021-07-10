from django.shortcuts import render,redirect
from django.http import Http404, HttpResponse, HttpResponseRedirect
from .models import Photos,Editor
import datetime as dt
from .forms import CreateUserForm
from django.contrib.auth.forms import UserCreationForm

def home(request):
    post=Photos.objects.all()
    editor=Editor.objects.all()
    date=dt.date.today()
    return render(request, 'main/home.html',{"post":post,"editor":editor,"date":date})

def registrationPage(request):
    form=CreateUserForm()
    
    if request.method=='POST':
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request,"registration/registration_form.html",{"form":form})
