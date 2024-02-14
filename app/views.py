from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.models import User ,auth
from django.contrib.auth import authenticate,get_user_model,logout
from .models import CustomUser
import json
from django.http import HttpResponse,JsonResponse
from django.core.paginator import Paginator
from itertools import chain
from .forms import CheckoutForm
from .models import CheckoutAddress
from django.views.generic import View
from django.core.exceptions import ObjectDoesNotExist

User = get_user_model()
def searchItem(request):
    brand_item =''
    category_item=''
    categories = Categories.objects.all()
    brands = Brands.objects.all()
    product = Product.objects.all()
    orderItem = OrderItem.objects.all()
    size = Size.objects.all()
    color = Color.objects.all()
    tags = Tags.objects.all()
    if request.user.is_authenticated:
        order = Order.objects.get(customer=request.user)
    else:
        order = Order.objects.all()
    nums = []
    value=''
    if request.method == 'POST':
        value = request.POST["item"]
    search_in_brand = Brands.objects.filter(brand__icontains=value)
    search_in_category = Categories.objects.filter(category__icontains=value)
  
    if search_in_brand:
        for i in search_in_brand:
            brand_item = Product.objects.filter(brand_id = i.id)    
    if search_in_category:
         for i in search_in_category:
            category_item = Product.objects.filter(category_id = i.id)  



    contact_list= list(chain(Product.objects.filter(product_name__icontains=value),brand_item,category_item ))
    paginator = Paginator(contact_list, 4) 
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    
    for i in range(1,page_obj.paginator.num_pages+1):
        nums.append(i)
    return render(request,'shop.html',{'nums':nums,
                                       'page_obj': page_obj,
                                       'product':product,
                                       'categories':categories,
                                       'brands':brands,
                                       'order':order,
                                       'OrderItem':orderItem,
                                       'size':size,
                                       'color':color,
                                       'tags':tags})
    
def index(request): 
    product = Product.objects.all()[0:4]
    product2 = Product.objects.all()[5:9]
    if request.user.is_authenticated: 
           
            customer = request.user
            order = Order.objects.get(customer=customer) 
            return render(request,'index.html',{'order':order,'product':product,'product2':product2})
    
    return render(request,'index.html',{'product':product,'product2':product2})

def about(request):
    if request.user.is_authenticated: 
            customer = request.user
            order = Order.objects.get(customer=customer) 
            return render(request,'about.html',{'order':order})
    return render(request,'about.html')

def blog_details(request):
    if request.user.is_authenticated: 
            customer = request.user
            order = Order.objects.get(customer=customer) 
            return render(request,'blog-details.html',{'order':order})
    return render(request,'blog-details.html')

def blog(request):
    if request.user.is_authenticated: 
            customer = request.user
            order = Order.objects.get(customer=customer) 
            return render(request,'blog.html',{'order':order})
    return render(request,'blog.html')

def checkout(request):
    if request.user.is_authenticated: 
            customer = request.user
            order = Order.objects.get(customer=customer) 
            items = order.orderitem_set.all()
            return render(request,'checkout.html',{'order':order,'items':items})
    return render(request,'checkout.html')

def contact(request):
    if request.user.is_authenticated: 
            customer = request.user
            order = Order.objects.get(customer=customer) 
            return render(request,'contact.html',{'order':order})
    return render(request,'contact.html')

def main(request):
    if request.user.is_authenticated: 
            customer = request.user
            order = Order.objects.get(customer=customer) 
            return render(request,'main.html',{'order':order})
    return render(request,'main.html')

def shop_details(request):
    if request.user.is_authenticated: 
            customer = request.user
            order = Order.objects.get(customer=customer) 
            return render(request,'shop-details.html',{'order':order})
    return render(request,'shop-details.html')

def shop(request):
    contact_list = Product.objects.all()
    paginator = Paginator(contact_list, 5) 
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    nums = []
    for i in range(1,page_obj.paginator.num_pages+1):
         nums.append(i)
    categories = Categories.objects.all()
    brands = Brands.objects.all()
    product = Product.objects.all()
    orderItem = OrderItem.objects.all()
    size = Size.objects.all()
    color = Color.objects.all()
    tags = Tags.objects.all()
    order = Order.objects.all()
    if request.user.is_authenticated: 
            customer = request.user
            order = Order.objects.get(customer=customer)
           
    return render(request,'shop.html',{'nums':nums,
                                       'page_obj': page_obj,
                                       'product':product,
                                       'categories':categories,
                                       'brands':brands,
                                       'order':order,
                                       'OrderItem':orderItem,
                                       'size':size,
                                        'color':color,
                                        'tags':tags})

def filterCategory(request,id):
    contact_list = Product.objects.filter(category_id=id)
    paginator = Paginator(contact_list, 2) 
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    nums = []
    for i in range(1,page_obj.paginator.num_pages+1):
         nums.append(i)
    categories = Categories.objects.all()
    brands = Brands.objects.all()
    product = Product.objects.all()
    size = Size.objects.all()
    tags = Tags.objects.all()
    color = Color.objects.all()
    orderItem = OrderItem.objects.all()
    if request.user.is_authenticated:
        order = Order.objects.get(customer=request.user)
    else:
        order = Order.objects.all()
    return render(request,'shop.html',{'page_obj':page_obj,
                                       'categories':categories,
                                       'brands':brands,
                                       'orderItem':orderItem,
                                       'product':product,
                                       'size':size,
                                       'color':color,
                                       'nums':nums,
                                       'tags':tags,
                                       'order':order})
     
def filterBrand(request,id):
    contact_list = Product.objects.filter(brand_id=id)
    paginator = Paginator(contact_list, 2) 
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    nums = []
    for i in range(1,page_obj.paginator.num_pages+1):
         nums.append(i)
    categories = Categories.objects.all()
    brands = Brands.objects.all()
    size = Size.objects.all()
    color = Color.objects.all()
    product = Product.objects.all()
    tags = Tags.objects.all()
    orderItem = OrderItem.objects.all()
    if request.user.is_authenticated:
        order = Order.objects.get(customer=request.user)
    else:
        order = Order.objects.all()
    return render(request,'shop.html',{'page_obj':page_obj,
                                       'categories':categories,
                                       'brands':brands,
                                       'orderItem':orderItem,
                                       'product':product,
                                       'size':size,
                                       'color':color,
                                       'nums':nums,
                                       'tags':tags,
                                       'order':order})

def filterSize(request,id):
    contact_list = Product.objects.filter(size_id=id)
    paginator = Paginator(contact_list, 3) 
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    nums = []
    for i in range(1,page_obj.paginator.num_pages+1):
         nums.append(i)
    categories = Categories.objects.all()
    brands = Brands.objects.all()
    product = Product.objects.all()
    size = Size.objects.all()
    color = Color.objects.all()
    tags = Tags.objects.all()
    orderItem = OrderItem.objects.all()
    if request.user.is_authenticated:
        order = Order.objects.get(customer=request.user)
    else:
        order = Order.objects.all()
    return render(request,'shop.html',{'page_obj':page_obj,
                                       'categories':categories,
                                       'brands':brands,
                                       'orderItem':orderItem,
                                       'product':product,
                                       'size':size,
                                       'color':color,
                                       'nums':nums,
                                       'tags':tags,
                                       'order':order})

def filterColor(request):
    print('isledim')
    if request.method == 'POST':
        print('isledim','2')
        name = request.POST["name"]
        name = int(name)
        print(name)
        contact_list = Product.objects.all()
        paginator = Paginator(contact_list, 3) 
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)
        nums = []
        for i in range(1,page_obj.paginator.num_pages+1):
            nums.append(i)
        categories = Categories.objects.all()
        brands = Brands.objects.all()
        product = Product.objects.all()
        size = Size.objects.all()
        color = Color.objects.all()
        orderItem = OrderItem.objects.all()
        page_obj = Product.objects.filter(color_id=name)
        return render(request,'shop.html',{'page_obj':page_obj,
                                        'categories':categories,
                                        'brands':brands,
                                        'orderItem':orderItem,
                                        'product':product,
                                        'size':size,
                                        'color':color}) 

def filterTag(request,id):
    contact_list = Product.objects.filter(tags_id=id)
    paginator = Paginator(contact_list, 3) 
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    nums = []
    for i in range(1,page_obj.paginator.num_pages+1):
        nums.append(i)
    categories = Categories.objects.all()
    brands = Brands.objects.all()
    product = Product.objects.all()
    size = Size.objects.all()
    color = Color.objects.all()
    tags = Tags.objects.all()
    orderItem = OrderItem.objects.all()
    if request.user.is_authenticated:
        order = Order.objects.get(customer=request.user)
    else:
        order = Order.objects.all()
    return render(request,'shop.html',{'page_obj':page_obj,
                                    'categories':categories,
                                    'brands':brands,
                                    'orderItem':orderItem,
                                    'product':product,
                                    'size':size,
                                    'color':color,
                                    'tags':tags,
                                    'nums':nums,
                                    'order':order}) 

def filterPrice(request):
    contact_list = Product.objects.order_by('product_price')
    paginator = Paginator(contact_list, 2) 
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    nums = []
    for i in range(1,page_obj.paginator.num_pages+1):
         nums.append(i)
    categories = Categories.objects.all()
    brands = Brands.objects.all()
    product = Product.objects.all()
    size = Size.objects.all()
    tags = Tags.objects.all()
    color = Color.objects.all()
    orderItem = OrderItem.objects.all()
    if request.user.is_authenticated:
        order = Order.objects.get(customer=request.user)
    else:
         order = Order.objects.all()
    return render(request,'shop.html',{'page_obj':page_obj,
                                       'categories':categories,
                                       'brands':brands,
                                       'orderItem':orderItem,
                                       'product':product,
                                       'size':size,
                                       'color':color,
                                       'nums':nums,
                                       'tags':tags,
                                       'order':order})

def filterForPrice(request,data):
    if data==50:
        contact_list = Product.objects.filter(product_price__range=(0,50))
    elif data==100:
        contact_list = Product.objects.filter(product_price__range=(50,100))
    elif data==150:
        contact_list = Product.objects.filter(product_price__range=(100,150))
    elif data==200:
        contact_list = Product.objects.filter(product_price__range=(150,200))
    elif data==250:
        contact_list = Product.objects.filter(product_price__range=(200,250))
    elif data==260:
        contact_list = Product.objects.filter(product_price__range=(251,100000))
    paginator = Paginator(contact_list, 2) 
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    nums = []
    for i in range(1,page_obj.paginator.num_pages+1):
         nums.append(i)
    categories = Categories.objects.all()
    brands = Brands.objects.all()
    product = Product.objects.all()
    size = Size.objects.all()
    tags = Tags.objects.all()
    color = Color.objects.all()
    orderItem = OrderItem.objects.all()
    if request.user.is_authenticated:
        order = Order.objects.get(customer=request.user)
    else:
        order = Order.objects.all()
    return render(request,'shop.html',{'page_obj':page_obj,
                                       'categories':categories,
                                       'brands':brands,
                                       'orderItem':orderItem,
                                       'product':product,
                                       'size':size,
                                       'color':color,
                                       'nums':nums,
                                       'tags':tags,
                                       'order':order})

def shopping_cart(request):
    items= ''
    if request.user.is_authenticated: 
            customer = request.user
            order, created = Order.objects.get_or_create(customer=customer, complete=False)
            items = order.orderitem_set.all()
    else:
            items = []
            order = Order.objects.all()
            # orderItem = OrderItem.objects.filter(order=order)
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
def updateItem(request): 
    customer = request.user
    order = Order.objects.get(customer=customer)
    orderItem = OrderItem.objects.all()
    contact_list = Product.objects.all()
    paginator = Paginator(contact_list, 5) 
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    nums = []
    for i in range(1,page_obj.paginator.num_pages+1):
        nums.append(i)
    product = Product.objects.all()
    data = ''
    productId = ''
    action= ''
    if request.method == 'POST':
        data = json.loads(request.body)
        customer = request.user
        productId = data['productId']
        action = data['action']
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
     
    
    return redirect('shopping-cart')       

def itemDelete(request,id):      
    customer = request.user
    product = Product.objects.get(id=id)
    order = Order.objects.get(customer=customer)
    orderItem = OrderItem.objects.get(order=order,product=product)
    orderItem.delete()
    return redirect('shopping-cart')
    # return render(request, 'shopping-cart.html')

def profile(request):
    pass

def searchCategory(request):
    pass
def update_cart_value(request):
    customer = request.user
    if request.method == "POST":
        data = json.loads(request.body)
        for item in data['data']['items']:
            product = Product.objects.get(id=item['itemId'])
            order, created = Order.objects.get_or_create(customer=customer,complete=False)
            orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)
            if int(item['itemValue'])>0:
                orderItem.quantity = item['itemValue']
                orderItem.save()
            else:
                orderItem.delete()
   
    
    return redirect('shopping-cart')
          

class CheckoutView(View):
    def get(self, *args, **kwargs):
        form = CheckoutForm()
        context = {
            'form': form
        }
        return render(self.request, 'checkout.html', context)

    def post(self, *args, **kwargs):
        form = CheckoutForm(self.request.POST or None)
        
        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            if form.is_valid():
                street_address = form.cleaned_data.get('street_address')
                apartment_address = form.cleaned_data.get('apartment_address')
                country = form.cleaned_data.get('country')
                zip = form.cleaned_data.get('zip')
                same_billing_address = form.cleaned_data.get('same_billing_address')
                save_info = form.cleaned_data.get('save_info')
                payment_option = form.cleaned_data.get('payment_option')

                checkout_address = CheckoutAddress(
                    user=self.request.user,
                    street_address=street_address,
                    apartment_address=apartment_address,
                    country=country,
                    zip=zip
                )
                checkout_address.save()
                order.checkout_address = checkout_address
                order.save()
                return redirect('core:checkout')
            messages.warning(self.request, "Failed Chekout")
            return redirect('core:checkout')

        except ObjectDoesNotExist:
            messages.error(self.request, "You do not have an order")
            return redirect("core:order-summary")