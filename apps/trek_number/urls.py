from django.urls import path
from .views import ProductView

app_name = "trek"

urlpatterns = [
    path('profile/', ProductView.as_view(), name='trek'),
]
