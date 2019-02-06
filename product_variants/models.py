
from django.db import models
from products.models import Products




# Create your models here.

class ProductVariants(models.Model):
	productid = models.ForeignKey(Products)
	size = models.CharField(max_length=255)
	color = models.CharField(max_length=255)
	material_type = models.CharField(max_length=255)
	gallery_photos = models.ImageField()
	quantity=models.IntegerField(default=0)
	createddate = models.DateTimeField(auto_now_add=True)
	modifieddate = models.DateTimeField(auto_now=True)
	
