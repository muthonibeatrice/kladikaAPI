
from django.db import models
from users.models import MyUser
from order.models import Order
from products.models import Products
from product_variants.models import ProductVariants
from django.db.models.signals import post_save
from django.db.models import F




# Create your models here.

class OrderedProducts(models.Model):
	
	userid = models.ForeignKey(MyUser)
	orderid = models.ForeignKey(Order)
	product_variantid = models.ForeignKey(Products, default=1)
	createddate = models.DateTimeField(auto_now_add=True)
	modifieddate = models.DateTimeField(auto_now=True)
	quantity = models.CharField(max_length=255)
	amount = models.CharField(max_length=255)
	
def deduct_stock(sender, **kwargs):
	print kwargs
	if kwargs['created']:
		instance=kwargs['instance']
		resp=ProductVariants.objects.filter(id=instance.product_variantid_id).update(quantity=F('quantity')-instance.quantity)
		print(resp)
post_save.connect(deduct_stock, sender=OrderedProducts)

   

