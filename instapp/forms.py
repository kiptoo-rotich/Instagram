from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from.models import Comment,Profile,Photos

class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username', 'email','password1','password2']

class CommentForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['comment'].widget = forms.TextInput()
        self.fields['comment'].widget.attrs['placeholder'] ='Add a comment...'
        
    class Meta:
        model=Comment
        fields = ('comment',)    

class profileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [ 'profilephoto', 'Bio']

class UserUpdate(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username','email'] 
    

class  NewPost(forms.ModelForm):
    class Meta:
        model = Photos
        exclude = ['pub_date', 'likes','profile']