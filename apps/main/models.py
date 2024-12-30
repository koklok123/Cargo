from django.db import models
from apps.telegram.utils import custom_upload_path
from django.urls import reverse
from django.utils import timezone
# Create your models here.

class Osnov(models.Model):
	trek_number = models.IntegerField(blank=True, null=True, verbose_name='Трек номер (необезатёльно)')

	name = models.CharField(max_length=50)
	job_title = models.CharField(max_length=50)
	description = models.TextField()
	image = models.ImageField(upload_to='images/')
	facebook = models.URLField()
	instagram = models.URLField()
	twitter = models.URLField()

	phone = models.SmallIntegerField(blank=True, null=True, verbose_name='Телефон (необезатёльно)')
	email = models.EmailField(blank=True, null=True, verbose_name='Почта (необезатёльно)')

	def __str__(self):
		return self.name
	
	class Meta:
		verbose_name = 'Основная информация'

class Questions(models.Model):
	vopros = models.TextField()
	otvet = models.TextField()

	def __str__(self):
		return self.vopros
	
	class Meta:
		verbose_name = 'Вопрос-ответ'




class News(models.Model):
    author = models.CharField(max_length=20)
    title = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    image_news = models.ImageField(upload_to='images_news/')
    image_author = models.ImageField(upload_to='images_author/')
    description = models.TextField(default='', blank=True, null=True)
    paragraph = models.TextField(verbose_name='Краткое описание события')
    slug = models.SlugField(max_length=255, unique=True, blank=True)

    def get_absolute_url(self):
        return reverse('news-list', kwargs={'slug': self.slug})


    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

class Comment(models.Model):
      name = models.CharField(max_length=30)
      email = models.EmailField()
      description = models.CharField(max_length=150)
      news = models.TextField()
    
      def __str__(self):
          return self.name

class Main(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Заголовок сайта'
    )
    description = models.TextField(
        verbose_name='Описание сайта'
    )
    logo = models.ImageField(
        upload_to=custom_upload_path
    )
    instagram = models.URLField(
        verbose_name='Ссылка на instagram',
        blank=True, null=True
    )
    facebook = models.URLField(
        verbose_name='Ссылка на facebook',
        blank=True, null=True
    )
    youtube = models.URLField(
        verbose_name='Ссылка на youtube',
        blank=True, null=True
    )
    
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = "Основная настройка"
        verbose_name_plural = "Основные настроки"
        

class Contact(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name="Имя отправителя"
    )
    email = models.EmailField(
        verbose_name="email"
    )
    subject = models.CharField(
        max_length=255,
        verbose_name="Тема отправителя"
    )
    message = models.TextField(
        verbose_name="Сообщение"
    )
    
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = "Оставленный отзыв"
        verbose_name_plural = "Оставденные отзывы"
        