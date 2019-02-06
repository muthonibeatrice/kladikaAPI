from django.db import models
from product_variants.models import ProductVariants
from django.db.models.signals import post_save
from django.db.models import F





# Create your models here.

class ProductStock(models.Model):
	product_variantid = models.ForeignKey(ProductVariants)
	quantity = models.IntegerField()
	createddate = models.DateTimeField(auto_now_add=True)
	modifieddate = models.DateTimeField(auto_now=True)



def add_stock(sender, **kwargs):
	print kwargs
	if kwargs['created']:
		instance=kwargs['instance']
		resp=ProductVariants.objects.filter(id=instance.product_variantid_id).update(quantity=F('quantity')+instance.quantity)
		print(resp)
post_save.connect(add_stock, sender=ProductStock)


