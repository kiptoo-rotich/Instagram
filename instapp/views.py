from django.shortcuts import render,redirect
from django.http import Http404, HttpResponse, HttpResponseRedirect
from .models import Photos,Editor
import datetime as dt

def home(request):
    post=Photos.objects.all()
    editor=Editor.objects.all()
    date=dt.date.today()
    return render(request, 'main/home.html',{"post":post,"editor":editor,"date":date})


