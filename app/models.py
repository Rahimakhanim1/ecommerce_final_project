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
    product_price = models.CharField(max_length = 100)
    product_image = models.FileField(upload_to = 'images/')
    category = models.ForeignKey(Categories,null = True,on_delete = models.DO_NOTHING)
    brand = models.ForeignKey(Brands,null = True,on_delete = models.DO_NOTHING)


    def __str__(self):
        return self.product_name


class CustomUser(AbstractUser):
    img = models.FileField(upload_to = "images/",null = True, blank = True)
    telephone = models.IntegerField(null = True,blank = True)
    address = models.CharField(null = True,blank = True, max_length = 100)



# Create your models here.
