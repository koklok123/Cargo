from django.shortcuts import render, redirect
from django.urls import reverse  
from django.views import View
from .models import Product

class ProductView(View):
    template_name = 'login/profile.html'
    
    def get(self, request):
        profile = {
            "user_name": "pon",
            "email": "pon@example.com",
            "articles": 10,
            "followers": 200,
            "rating": 4.9
        }

        orders = Product.objects.all()
        return render(request, self.template_name, {"profile": profile, "orders": orders})

    def post(self, request):
        product_name = request.POST.get('product_name')
        tracking_number = request.POST.get('tracking_number')

        Product.objects.create(
            product=product_name,
            trek_number=tracking_number,
            status=False
        )

       
        return redirect(reverse('trek:trek'))
