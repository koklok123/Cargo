from django.db import models

# Create your models here.
class Trek(models.Model):
    #трек номер который вводиться из админки а там с акаунта
    trek_number = models.IntegerField(verbose_name='Трек номер')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  
        product = Product.objects.filter(trek_number=self.trek_number).first()
        if product:
            product.status = True  
            product.save()  


class Product(models.Model):
    #id используеться как номер заказа
    id = models.AutoField(primary_key=True)  
    product = models.CharField(max_length=80, verbose_name='Товар')
    status = models.BooleanField(default=False, verbose_name='Статус')
    trek_number = models.IntegerField(verbose_name='Трек номер')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return f"Заказ {self.id}: {self.product} - {'Активен' if self.status else 'Неактивен'}"