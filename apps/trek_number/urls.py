from django.urls import path
from .views import ProductView

urlpatterns = [
    path('profile/', ProductView.as_view(), name='profile'),
    path('profile/create_order/', ProductView.as_view(), name='create_order'),
]
