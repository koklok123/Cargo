from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'trek_number', 'status', 'date')
    list_filter = ('status',)
    search_fields = ('trek_number',)



admin.site.register(Product, ProductAdmin)
