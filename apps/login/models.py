import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models
# Create your models here.


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    confirmation_code = models.UUIDField(default=uuid.uuid4, editable=False)
    is_email_confirmed = models.BooleanField(default=False)

class Profile(models.Model):
    user_name = models.CharField(max_length=30)
    email = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    position = models.CharField(verbose_name='Ваша должность', max_length=40)
    image_profile = models.ImageField(upload_to='profile')
    articles = models.IntegerField(verbose_name='Статьи')
    followers = models.IntegerField(verbose_name='Подпищики')
    rating = models.FloatField(verbose_name='Рейтинг')