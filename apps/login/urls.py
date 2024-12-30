from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('confirm-email/<uuid:code>/', views.confirm_email, name='confirm_email'),
    path('login/', auth_views.LoginView.as_view(template_name='auth/login.html'), name='login'),  # Вход
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),  # Выход
    path('profile/', views.profile, name='profile'),  # Профиль
]