from django.contrib import admin
from .models import Editor,Photos,tags

class ArticleAdmin(admin.ModelAdmin):
    filter_horizontal=('tags')

admin.site.register(Editor) 
admin.site.register(Photos) 
admin.site.register(tags) 
