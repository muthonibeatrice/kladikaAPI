
from django.db import models





# Create your models here.

class Order(models.Model):
	
	ordername = models.CharField(max_length=255)
	payment_choices = ( 
		('cod', 'Cash_On_Delivery'), 
		('pesapal', 'Pesapal'),
		('mpesa', 'M-Pesa') 
		)
	mode_of_payment= models.CharField(choices=payment_choices, max_length=255)
	total = models.CharField(max_length=255)
	payment_status = models.CharField(max_length=255)
	amount_paid= models.CharField(max_length=255)
	createddate = models.DateTimeField(auto_now_add=True)
	modifieddate = models.DateTimeField(auto_now=True)
	

