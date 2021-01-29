from django.urls import path
from news.views import *

app_name = 'news'

urlpatterns = [
    path('it/', ItNews, name='it'),
    path('sport/', SportNews, name='sport'),
    path('economy/', EconomyNews, name='economy'),
    path('stock/', Stockview, name='stock'),
]