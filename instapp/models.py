from django.db import models
from tinymce.models import HTMLField
import datetime as dt
from django.contrib.auth.models import User


class Photos(models.Model):
    title = models.CharField(max_length=60)
    post = models.TextField(max_length=1000)
    pub_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/', default="Image")
    likes = models.ManyToManyField(User, related_name='post_like')
    user = models.ForeignKey(User, blank=True,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.post)[:10]

    def number_of_likes(self):
        return self.likes.count()


class tags(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Comment(models.Model):
    comment = models.TextField()
    image = models.ForeignKey(Photos, on_delete=models.CASCADE)
    posted_on = models.DateTimeField(auto_now_add=True, null=True)

    def save_comment(self):
        self.save()

    def delete(self):
        self.delete()


class Profile(models.Model):
    profilephoto = models.ImageField('image')
    Bio = models.CharField(max_length=30)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    following = models.ManyToManyField(User, blank=True, related_name='follow')

    def __str__(self):
        return self.Bio

    def delete_profile(self):
        self.delete()

    def save_profile(self):
        self.save()

    @classmethod
    def search_profile(cls, name):
        return cls.objects.filter(user__username__icontains=name).all()

