from django.db import models
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



# Create your models here.
