from django.contrib import admin
from . models import Trek, Product
# Register your models here.

# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):

#     list_display = ['id', 'product', 'status', 'trek_number', 'date']
#     list_filter = ['status', 'date']
#     search_fields = ['product', 'trek_number']

@admin.register(Trek)
class TrekAdmin(admin.ModelAdmin):
    list_display = ['id', 'trek_number']
