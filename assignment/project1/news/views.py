from django.shortcuts import render

# Create your views here.
from news.models import News
from django.views.generic import ListView

class NewsLV(ListView):
    model = News
    template_name = "news/news_take.html"
    context_object_name = "newses"
    paginate_by = 10