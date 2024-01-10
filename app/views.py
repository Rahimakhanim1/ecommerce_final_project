from django.shortcuts import render
from .models import *

def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def blog_details(request):
    return render(request,'blog-details.html')

def blog(request):
    return render(request,'blog.html')


def checkout(request):
    return render(request,'checkout.html')

def contact(request):
    return render(request,'contact.html')

def main(request):
    return render(request,'main.html')

def shop_details(request):
    return render(request,'shop-details.html')

def shop(request):
    product = Product.objects.all()
    return render(request,'shop.html',{'product':product})

def shopping_cart(request):
    return render(request,'shopping-cart.html')

# Create your views here.
