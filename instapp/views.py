from django.shortcuts import render,redirect
from django.http import Http404, HttpResponse, HttpResponseRedirect

def home(request):
    return render(request, 'main/home.html')
