from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.models import User ,auth
from django.contrib.auth import authenticate,get_user_model,logout
from .models import CustomUser
from django.http import JsonResponse
import json
User = get_user_model()

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
    Customuser = CustomUser.objects.all()
    if request.method == 'POST':       
        username = request.POST["username"]
        password = request.POST["password"]              
        # form = RecaptchaForm(request.POST)
        
        # if form.is_valid():    
        user = authenticate(username=username,password=password)
            
        if user is not None:
            auth.login(request,user)
            return render(request,"index.html",{'user':user,'CustomUser': Customuser})
   
    return render(request,'signin.html')
            
def register(request):
    
    if request.method == 'POST':
        

        username = request.POST["name"]
        first_name = request.POST["firstname"]
        foto = request.FILES["foto"]
        last_name = request.POST["lastname"]
        email = request.POST["email"]
        pass1 = request.POST["password"]
        pass2 = request.POST["re-password"]
        telephone = request.POST["tel"]
        address = request.POST["address"]
        tel = str(telephone)
        correct_tel = ''
        for i in tel:
            if i.isnumeric():
                correct_tel+=i
        correct_tel=int(correct_tel)


        
        if pass1 == pass2:
            
            if CustomUser.objects.filter(username=username).exists():
                messages.error(request,"Bu istifadəçi hal-hazırda mövcuddur")
            elif CustomUser.objects.filter(email=email).exists():
                messages.error(request,"Bu email hal-hazırda mövcuddur")
            else:
                
                CustomUser.objects.create_user(username=username,
                                               email=email, 
                                               password=pass1,
                                               first_name=first_name,
                                               last_name=last_name,
                                               img=foto,
                                               telephone=correct_tel,
                                               address = address).save()
                # return redirect("login")
                return render(request,"register.html")
            
        else:
            messages.error(request,"Şifrələr uyğun deyil")
            
        
    
    return render(request,"register.html")


def signout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully!!")
    return redirect('index')


def updateItem(request):
    data = json.loads(request.data)
    productId = data['productId']
    action = data['action']
    print('aCtion',action)
    print(data)
    print('salam')
    return JsonResponse('Item was added', safe=False )
def profile(request):
    pass
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
