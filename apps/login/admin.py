from django.contrib import admin
from django.contrib.auth.models import User
from . models import Profile

# Register your models here.
admin.site.register(User)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user_name', 'position', 'email', 'image_profile', 'articles', 'followers', 'rating']