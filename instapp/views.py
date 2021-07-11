from django.shortcuts import render,redirect
from django.http import Http404, HttpResponse, HttpResponseRedirect
from .models import Photos,Editor,Comment
import datetime as dt
from django.shortcuts import get_object_or_404
from .forms import CreateUserForm,CommentForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


@login_required(login_url='/accounts/login/')
def home(request):
    post=Photos.objects.all()
    editor=User.objects.all()
    date=dt.date.today()
    current_user = request.user
    return render(request, 'main/home.html',{"post":post,"editor":editor,"date":date,"current_user":current_user})


def registrationPage(request):
    form=CreateUserForm()
    
    if request.method=='POST':
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request,"registration/registration_form.html",{"form":form})

def comment(request,id):
    comment=Comment.objects.filter(image=id)
    image=Photos.objects.filter(image=id).all()
    current_user=request.user
    image=get_object_or_404(Photos,id=id)
    if request.method=='POST':
        commentForm=CommentForm(request.POST)
        if commentForm.is_valid():
            comment=commentForm.save(commit=False)
            comment.image=image
            comment.save()
            return HttpResponseRedirect(request.path_info)
    else:
        commentForm=CommentForm()
    return render(request,'main/comment.html',{"commentForm":commentForm,"comment":comment,"image":image})

def profile(request):
    if request.method == 'POST':

        userForm = UserUpdate(request.POST, instance=request.user)
        profile_form = profileForm(
            request.POST, request.FILES, instance=request.user)

        if  profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('home')
    else:
        profile_form = profileForm(instance=request.user)
        user_form = UserUpdate(instance=request.user)

        display = {
            'user_form':user_form,
            'profile_form': profile_form
        }

    return render(request, 'main/profile.html', display)