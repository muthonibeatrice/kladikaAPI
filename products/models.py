
from django.db import models
from store.models import Store
from product_type.models import ProductType
from product_subtype.models import ProductSubType



# Create your models here.


class Products(models.Model):
	storeid= models.ForeignKey(Store)
	product_typeid= models.ForeignKey(ProductType)
	product_subtypeid= models.ForeignKey(ProductSubType)
	productname = models.CharField(max_length=255)
	product_description = models.CharField(max_length=255)
	feature_photo = models.ImageField()
	regular_price = models.CharField(max_length=255)
	sale_price = models.CharField(max_length=255, null=True, blank=True)
	createddate = models.DateTimeField(auto_now_add=True)
	modifieddate = models.DateTimeField(auto_now=True)
	


