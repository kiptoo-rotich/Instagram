from django.db import models
from tinymce.models import HTMLField
import datetime as dt
from django.contrib.auth.models import User


class Editor(models.Model):
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)
    email = models.EmailField()
    phone_number = models.CharField(max_length=10, blank=True)

    def _str_(self):
        return self.first_name

    def save_editor(self):
        self.save()

class Photos(models.Model):
    title = models.CharField(max_length=60)
    post=models.TextField(max_length=1000)
    pub_date=models.DateTimeField(auto_now_add=True)
    editor = models.ForeignKey('Editor',on_delete=models.CASCADE,)
    image=models.ImageField(upload_to='images/', default="Image")

    def __str__(self):
        return str(self.post)[:10]
    
class tags(models.Model):
    name=models.CharField(max_length=30)
    
    def __str__(self):
        return self.name