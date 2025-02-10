from django.db import models

class Product(models.Model):
    STATUS_CHOICES = [
        (True, 'Пришло'),   
        (False, 'Не пришло') 
    ]

    #id используеться как номер заказа
    id = models.AutoField(primary_key=True)  
    product = models.CharField(max_length=80, verbose_name='Товар')
    status = models.BooleanField(default=False, verbose_name='Статус', choices=STATUS_CHOICES)
    trek_number = models.IntegerField(verbose_name='Трек номер', unique=True)
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return f"Заказ {self.id}: {self.product} - {'Пришло' if self.status else 'Не пришло'}"
