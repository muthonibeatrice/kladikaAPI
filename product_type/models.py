
from django.db import models



# Create your models here.

class ProductType(models.Model):
	   type_choices = (('Men', 'Menswear'), ('Women', 'Ladieswear'), ('Kids', 'Kidswear'))
	   types= models.CharField(choices=type_choices, max_length=255)
	   createddate = models.DateTimeField(auto_now_add=True)
	   modifieddate = models.DateTimeField(auto_now=True)
	
	