from django.contrib import admin
from .models import Profile, Photos,tags

class ArticleAdmin(admin.ModelAdmin):
    filter_horizontal=('tags')

admin.site.register(Profile) 
admin.site.register(Photos) 
admin.site.register(tags) 
