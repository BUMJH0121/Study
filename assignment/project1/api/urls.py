from django.contrib import admin
from django.urls import path, include
from project1.views import HomeView
from api.views import UserViewSet
from rest_framework import routers

routers = routers.DefaultRouter()
routers.register('news',UserViewSet)


urlpatterns = [
    path('', include(routers.urls)),
]