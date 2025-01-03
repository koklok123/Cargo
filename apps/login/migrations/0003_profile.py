# Generated by Django 5.1.4 on 2024-12-30 10:58

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_customuser_confirmation_code_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=30)),
                ('position', models.CharField(max_length=40, verbose_name='Ваша должность')),
                ('image_profile', models.ImageField(upload_to='profile')),
                ('articles', models.IntegerField(verbose_name='Статьи')),
                ('followers', models.IntegerField(verbose_name='Подпищики')),
                ('rating', models.FloatField(verbose_name='Рейтинг')),
                ('email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
