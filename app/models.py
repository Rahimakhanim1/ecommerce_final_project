from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser
class Categories(models.Model):
    category = models.CharField(max_length = 50,null = True)

    def __str__(self):
        return self.category
  

    
class Brands(models.Model):
    brand = models.CharField(max_length = 50, null = True)

    def __str__(self):
        return self.brand
    
class Product(models.Model):
    product_name = models.CharField(max_length = 100)
    product_price = models.FloatField(blank = True)
    product_image = models.FileField(upload_to = 'images/')
    category = models.ForeignKey(Categories,null = True,on_delete = models.DO_NOTHING)
    brand = models.ForeignKey(Brands,null = True,on_delete = models.DO_NOTHING)


    def __str__(self):
        return self.product_name
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


class CustomUser(AbstractUser):
    img = models.FileField(upload_to = "images/",null = True, blank = True)
    telephone = models.IntegerField(null = True,blank = True)
    address = models.CharField(null = True,blank = True, max_length = 100)

class Order(models.Model):
    customer = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, blank=True, null=True)
    data_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=200, null=True)

    def _str__(self):
        return str(self.id)
    
    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return round(total,2)
   
    @property 
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total 

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True,null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    data_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.product.product_price * self.quantity 
        return round(total,2)
# Create your models here.
