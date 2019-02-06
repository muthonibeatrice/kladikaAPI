
from django.db import models
from products.models import Products
from users.models import MyUser



# Create your models here.

class MyStyle(models.Model):
	productid = models.ForeignKey(Products)
	userid = models.ForeignKey(MyUser)
	createddate = models.DateTimeField(auto_now_add=True)
	modifieddate = models.DateTimeField(auto_now=True)

  