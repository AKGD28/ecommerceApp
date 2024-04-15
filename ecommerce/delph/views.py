from django.http import HttpResponse
from django.shortcuts import render

def about_view(request):
    return render(request, 'about.html')

def contact_view(request):
    return render(request, 'contact.html')

def index_view(request):
    return render(request, 'index.html')

def shop_single_view(request):
    return render(request, 'shop-single.html')

def shop_view(request):
    return render(request, 'shop.html')


