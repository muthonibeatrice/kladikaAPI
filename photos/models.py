
from django.db import models
from merchant.models import Merchant


# Create your models here.

class Photos(models.Model):
	merchantid = models.ForeignKey(Merchant)
	photoid  = models.CharField(max_length=255)
	photos = models.ImageField()
	createddate = models.DateTimeField(auto_now_add=True)
	modifieddate = models.DateTimeField(auto_now=True)


    