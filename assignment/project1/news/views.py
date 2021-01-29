from django.shortcuts import render
from django.urls import reverse
from django.db.models import Q
import os
# Create your views here.
from news.models import News
from django.views.generic import ListView,FormView




def ItNews(request):
    context = {}
    if 'kind' in request.GET:
        os.chdir('/Users/bumjh/Desktop/Study/assignment/project1/Itnews')
        os.system('scrapy crawl itbots')
        temp = News.objects.filter(Q(kind__icontains="IT"))
        context = {'News' : temp}
    return render(request, 'news/news_it.html', context)


def SportNews(request):
    context = {}
    if 'kind' in request.GET:
        os.chdir('/Users/bumjh/Desktop/Study/assignment/project1/Itnews')
        os.system('scrapy crawl sportbots')
        temp = News.objects.filter(Q(kind__icontains="SPORT"))
        context = {'News' : temp}
    return render(request, 'news/news_sport.html', context)
    

def EconomyNews(request):
    context = {}
    if 'kind' in request.GET:
        os.chdir('/Users/bumjh/Desktop/Study/assignment/project1/Itnews')
        os.system('scrapy crawl economybots')
        temp = News.objects.filter(Q(kind__icontains="ECONOMY"))
        context = {'News' : temp}
    return render(request, 'news/news_economy.html', context)

def Stockview(request):
    context = {}
    if request.method == 'GET':
        if 'name' in request.GET:
            temp = request.GET['name']
            stock = News.objects.filter(Q(kind__icontains="STOCK"))
            context = {'Stock' : stock}
    return render(request, 'news/stock.html', context)