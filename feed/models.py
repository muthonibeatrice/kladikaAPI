
from django.db import models
from ordered_products.models import OrderedProducts
from users.models import MyUser



# Create your models here.

class Feed(models.Model):
	ordered_productsid = models.ForeignKey(OrderedProducts)
	userid = models.ForeignKey(MyUser)
	uphoto = models.ImageField()
	caption = models.CharField(max_length=255)
	createddate = models.DateTimeField(auto_now_add=True)
	modifieddate = models.DateTimeField(auto_now=True)
	