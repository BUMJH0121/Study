from django.urls import path
from weather.views import *

app_name = 'weather'

urlpatterns = [
    path('', Search, name="weather_search"),
]