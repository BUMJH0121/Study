from django.shortcuts import render
from django.urls import reverse
from django.db.models import Q
import os
import urllib
import json
# Create your views here.
from news.models import News
from django.views.generic import ListView,FormView

# Create your views here.
def Search(request):
    context = {}
    if request.method == 'GET':
        if 'city' in request.GET:
            temp = request.GET['city']
            client_key = "9d4bd7ac6c4ca6ea0d7872755dc9af77"
            api_call = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}&lang=kr".format(temp, client_key)
            req = urllib.request.urlopen(api_call)
            if req.getcode() == 200:
                body = req.read()
                result = json.loads(body.decode('utf-8'))
                context = {'weather' : result}
    return render(request, 'weather/weather_search.html', context)