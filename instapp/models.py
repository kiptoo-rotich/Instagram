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

class photos(models.Model):
    title = models.CharField(max_length=60)
    post=HTMLField()
    # tags=models.ManyToManyField(tags)
    pub_date=models.DateTimeField(auto_now_add=True)
    editor = models.ForeignKey(User,on_delete=models.CASCADE,)
    image=models.ImageField(upload_to='articles/', default="Image")

    def __str__(self):
        return self.title
    
class tags(models.Model):
    name=models.CharField(max_length=30)
    
    def __str__(self):
        return self.name