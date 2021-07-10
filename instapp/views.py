from django.shortcuts import render,redirect
from django.http import Http404, HttpResponse, HttpResponseRedirect
from .models import Photos,Editor

def home(request):
    post=Photos.objects.all()
    editor=Editor.objects.all()
    return render(request, 'main/home.html',{"post":post,"editor":editor})


