from django.contrib import admin
from .models import Osnov, Questions, News, Comment

@admin.register(Osnov)
class OsnovAdmin(admin.ModelAdmin):
	list_display = ('name', 'job_title', 'description', 'image', 'facebook', 'instagram', 'twitter',  'phone', 'email')

@admin.register(Questions)
class QuestionsAdmin(admin.ModelAdmin):
	list_display = ['vopros', 'otvet']

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['time', 'author', 'title', 'description', 'image_news', 'image_author', 'paragraph']
    prepopulated_fields = {'slug': ['title',]}

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'description', 'news']
    
