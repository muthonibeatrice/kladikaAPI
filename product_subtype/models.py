from django.db import models
from product_type.models import ProductType



# Create your models here.

class ProductSubType(models.Model):
	   product_typeid= models.ForeignKey(ProductType)
	   subtype_choices=(
		('suits', 'Suits'),
		('khaki_pants', 'Khaki_pants'), 
		('accessories', 'Accessories'),
		('shirts', 'Shirts'),
		('dresses', 'Dresses'),
		('tops', 'Tops'),
		('skirts', 'Skirts'),
		('jeans', 'Jeans'),
		('jewellery', 'Jewellery'),
		('handbags', 'Handbags'),
		('shoes', 'Shoes')
		)
	   subtypes = models.CharField(choices=subtype_choices, max_length=255)
	   createddate = models.DateTimeField(auto_now_add=True)
	   modifieddate = models.DateTimeField(auto_now=True)
	
	