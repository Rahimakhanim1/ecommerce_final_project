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
    orderItem = OrderItem.objects.all()
    if request.user.is_authenticated: 
            customer = request.user
            order = Order.objects.get(customer=customer)
    # categoriesCount = []
    # for c_item in categories:
    #     count = Product.objects.filter(category_id = c_item).count()
       
    #     categoriesCount.append(count)     
    return render(request,'shop.html',{'product':product,'categories':categories,'brands':brands,'order':order,'OrderItem':orderItem})

def shopping_cart(request):
    items= ''
    if request.user.is_authenticated: 
            customer = request.user
            order, created = Order.objects.get_or_create(customer=customer, complete=False)
            items = order.orderitem_set.all()
    else:
            items = []
   
    orderItem = OrderItem.objects.all()
    context= {'items': items,'order':order}
    return render(request, 'shopping-cart.html', context)

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
# def store(request):
#     products = Product.objects.all()
#     context = {'products' : products}
#     return render(request, 'shop.html',context)

# def cart(request):
#     if request.user.is_authenticated:
#         customer = request.user
#         order, created = Order.objects.get_or_create(customer=customer, complete=False)
#         items = order.orderItem_set.all()
#     else:
#         items = []
#         order = {'get_cart_total':0, 'get_cart_items':0 }
#     context = {'items':items, 'order':order}

#     return render(request,'shopping-cart.html',context)

# def checkout(request):
#     if request.user.is_authenticated:
#         customer = request.user
#         order, created = Order.objects.get_or_create(customer=customer, complete=False)
#         items = order.orderItem_set.all()
#     else:
#         items = []
#         order = {'get_cart_total':0, 'get_cart_items':0 }
#     context = {'items':items, 'order':order}

#     return render(request,'shopping-cart.html',context)
# def cart(request):
#     items= ''
#     print('isledim')
#     if request.method == 'POST':
#         if request.user.is_authenticated:
#             print('isleyirme')
#             customer = request.user
#             order, created = Order.objects.get_or_create(customer=customer, complete=False)
#             items = order.orderitem_set.all()
#         else:
#             print('islemirem')
#             items = []
#     a = Product.objects.all()
#     context= {'items': items,'a':a}
#     print(context)
#     return render(request, 'shopping-cart.html', context)

def updateItem(request):
    data = ''
    productId =''
    action= ''
    if request.method == 'POST':
        data = json.loads(request.body)
        productId = data['productId']
        action = data['action']
        customer = request.user
        product = Product.objects.get(id=productId)
        order, created = Order.objects.get_or_create(customer=customer,complete=False)
        orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)
        
        if action == 'add':
            orderItem.quantity = (orderItem.quantity + 1)
        elif action == 'remove':
            orderItem.quantity = (orderItem.quantity - 1)
        orderItem.save()
        
        if orderItem.quantity <= 0:
            orderItem.delete()
     

        return redirect('shop')


    return redirect('shop')

def updateItemForShoppingCart(request):
    data = ''
    productId =''
    action= ''
    if request.method == 'POST':
        data = json.loads(request.body)
        productId = data['productId']
        action = data['action']
        customer = request.user
        product = Product.objects.get(id=productId)
        order, created = Order.objects.get_or_create(customer=customer,complete=False)
        orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

   
            
        # if action == 'add':
        #     orderItem.quantity = (orderItem.quantity + 1)
        # elif action == 'remove':
        #     orderItem.quantity = (orderItem.quantity - 1)
        # orderItem.save()
        
        if orderItem.quantity <= 0:
            orderItem.delete()
        return redirect('shopping-cart')
    order = Order.objects.all()
    orderItem = OrderItem.objects.all()
    categories = Categories.objects.all()
    brands = Brands.objects.all()
    product = Product.objects.all()
    return redirect('shopping-cart')

def itemDelete(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        productId = data['productId']
        action = data['action']
        if action=='remove':
            customer = request.user
            product = Product.objects.get(id=productId)
            order= Order.objects.get(customer=customer)
            orderItem = OrderItem.objects.get(order=order,product=product)
            orderItem.delete()
    return redirect('shopping-cart')
    # return render(request, 'shopping-cart.html')

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
