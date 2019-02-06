from django.db import models
from merchant.models import Merchant




# Create your models here.

class Store(models.Model):
	merchantid = models.ForeignKey(Merchant)
	storename = models.CharField(max_length=255)
	email = models.EmailField(max_length=255)
	location = models.CharField(max_length=255)
	phonenumber = models.CharField(max_length=255)
	createddate = models.DateTimeField(auto_now_add=True)
	modifieddate = models.DateTimeField(auto_now=True)
	


	def __str__(self):
			return self.storename