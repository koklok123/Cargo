from django.shortcuts import render
from django.views import View

# Create your views here.
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
        orders = [
            {"number": 1234, "product_name": "Смартфон iPhone 13", "status": "delivered", "tracking_number": "RU123456789", "date": "2024-01-15"},
            {"number": 1235, "product_name": "Ноутбук Dell XPS 13", "status": "pending", "tracking_number": "RU987654321", "date": "2024-01-20"},
        ]
        return render(request, self.template_name, {"profile": profile, "orders": orders})

    def post(self, request):
        pass
        return render(request, self.template_name)
