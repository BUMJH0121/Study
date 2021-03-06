"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

from mysite.views import HomeView
from rest_framework import routers
from blog import rest_views

router = routers.DefaultRouter()
router.register(r'users', rest_views.UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),

    # http://127.0.0.1:8000/ -> home page 
    path('', HomeView.as_view(), name='home'),

    path('bookmark/', include('bookmark.urls', namespace='bookmark')),
    path('blog/', include('blog.urls', namespace='blog')),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='blog')),
]
