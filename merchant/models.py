
from django.db import models



# Create your models here.

class Merchant(models.Model):
	#merchantid = models.CharField(max_length=255, default='DEFAULT VALUE')
	merchantname = models.CharField(max_length=255)
	krapin = models.CharField(max_length=255)
	email = models.EmailField(max_length=255)
	phonenumber = models.CharField(max_length=255)
	createddate = models.DateTimeField(auto_now_add=True)
	modifieddate = models.DateTimeField(auto_now=True)
	
	def __str__(self):
		return self.merchantname
	

