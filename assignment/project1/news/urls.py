from django.urls import path
from news.views import *

app_name = 'news'

urlpatterns = [
    path('', NewsLV.as_view(), name='take'),
]