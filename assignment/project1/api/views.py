from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from news.serializers import UserSerializer
from news.models import News

class UserViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = UserSerializer