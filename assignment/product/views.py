from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def product_list(request):
    return render(request,'product/product_list.html')