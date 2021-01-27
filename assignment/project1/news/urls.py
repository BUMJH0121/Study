from django.urls import path
from news.views import *

app_name = 'news'

urlpatterns = [
    path('it/', ItNewsDV.as_view(), name='it'),
    path('sport/', SportNewsDV.as_view(), name='sport'),
    path('economy/', EconomyNewsDV.as_view(), name='economy'),
]