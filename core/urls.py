"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from apps.main.views import custum_404_view, custum_500_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('', include('apps.main.urls')),
    path('login/', include('apps.login.urls')),
    path('prof/', include('apps.trek_number.urls')),
    path('404/', custum_404_view),
    path('500/', custum_500_view),
]

# HTTP ошибки
handler404 = 'apps.main.views.custum_404_view'
handler500 = 'apps.main.views.custum_500_view'
# handler403 = 'apps.main.views.custum_403_view'

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
