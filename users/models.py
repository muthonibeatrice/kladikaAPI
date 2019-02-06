
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save


# Create your models here.


class MyUser(AbstractUser):
	location = models.CharField(max_length=255)
	phonenumber = models.CharField(max_length=255)
	# age = models.DateField()
	occupation =  models.CharField(max_length=255)
	createddate = models.DateTimeField(auto_now_add=True)
	modifieddate = models.DateTimeField(auto_now=True)
	
    

