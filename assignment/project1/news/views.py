from django.shortcuts import render

# Create your views here.
from news.models import News
from django.views.generic import ListView


class ItNewsDV(ListView):
    model = News
    context_object_name = "itnews"
    template_name = "news/news_it.html"
    paginate_by = 10


class SportNewsDV(ListView):
    model = News
    context_object_name = "sportnews"
    template_name = "news/news_sport.html"
    paginate_by = 10
    
class EconomyNewsDV(ListView):
    model = News
    context_object_name = "economynews"
    template_name = "news/news_economy.html"
    paginate_by = 10
    