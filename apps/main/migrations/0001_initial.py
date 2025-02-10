# Generated by Django 5.1.4 on 2025-02-07 14:08

import apps.telegram.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('description', models.CharField(max_length=150)),
                ('news', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Имя отправителя')),
                ('email', models.EmailField(max_length=254, verbose_name='email')),
                ('subject', models.CharField(max_length=255, verbose_name='Тема отправителя')),
                ('message', models.TextField(verbose_name='Сообщение')),
            ],
            options={
                'verbose_name': 'Оставленный отзыв',
                'verbose_name_plural': 'Оставденные отзывы',
            },
        ),
        migrations.CreateModel(
            name='Main',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок сайта')),
                ('description', models.TextField(verbose_name='Описание сайта')),
                ('logo', models.ImageField(upload_to=apps.telegram.utils.custom_upload_path)),
                ('instagram', models.URLField(blank=True, null=True, verbose_name='Ссылка на instagram')),
                ('facebook', models.URLField(blank=True, null=True, verbose_name='Ссылка на facebook')),
                ('youtube', models.URLField(blank=True, null=True, verbose_name='Ссылка на youtube')),
            ],
            options={
                'verbose_name': 'Основная настройка',
                'verbose_name_plural': 'Основные настроки',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=20)),
                ('title', models.TextField()),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('image_news', models.ImageField(upload_to='images_news/')),
                ('image_author', models.ImageField(upload_to='images_author/')),
                ('description', models.TextField(blank=True, default='', null=True)),
                ('paragraph', models.TextField(verbose_name='Краткое описание события')),
                ('slug', models.SlugField(blank=True, max_length=255, unique=True)),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
            },
        ),
        migrations.CreateModel(
            name='Osnov',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trek_number', models.IntegerField(blank=True, null=True, verbose_name='Трек номер (необезатёльно)')),
                ('name', models.CharField(max_length=50)),
                ('job_title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='images/')),
                ('facebook', models.URLField()),
                ('instagram', models.URLField()),
                ('twitter', models.URLField()),
                ('phone', models.SmallIntegerField(blank=True, null=True, verbose_name='Телефон (необезатёльно)')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Почта (необезатёльно)')),
            ],
            options={
                'verbose_name': 'Основная информация',
            },
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vopros', models.TextField()),
                ('otvet', models.TextField()),
            ],
            options={
                'verbose_name': 'Вопрос-ответ',
            },
        ),
    ]
