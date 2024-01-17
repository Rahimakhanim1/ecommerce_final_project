from django.shortcuts import render
from .models import *
from django.db.models import Q

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
    categories = Categories.objects.all()
    brands = Brands.objects.all()
    product = Product.objects.all()
    # categoriesCount = []
    # for c_item in categories:
    #     count = Product.objects.filter(category_id = c_item).count()
       
    #     categoriesCount.append(count)
    
        
    return render(request,'shop.html',{'product':product,'categories':categories,'brands':brands})

def shopping_cart(request):
    return render(request,'shopping-cart.html')
def sign_in(request):
    return render(request,'signin.html')

# def filterCat(request,id):
#     filterData = Product.objects.filter(category_id = id)
#     categories = Categories.objects.all()
#     brands = Brands.objects.all()
#     return render(request,'shop.html',{'filterData':filterData,'categories':categories,'brands':brands})

# def filterBrand(request,id):
#     filterBata = Product.objects.filter(brand_id = id)
#     categories = Categories.objects.all()
#     brands = Brands.objects.all()
#     return render(request,'shop.html',{'filterData':filterBata,'categories':categories,'brands':brands})



# Create your views here.
