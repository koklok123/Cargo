# Generated by Django 5.1.4 on 2024-12-29 11:18

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='confirmation_code',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
        migrations.AddField(
            model_name='customuser',
            name='is_email_confirmed',
            field=models.BooleanField(default=False),
        ),
    ]
