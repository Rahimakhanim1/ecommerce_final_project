from django.db import models

class Product(models.Model):
    product_name = models.CharField(max_length = 100)
    product_price = models.CharField(max_length = 100)
    product_image = models.FileField(upload_to = 'images/')

# Create your models here.
