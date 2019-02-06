
from django.db import models
from order.models import Order
from django.db.models.signals import post_save
from django.db.models import F



# Create your models here.

class Payment(models.Model):
	order = models.ForeignKey(Order)
	amount_paid  = models.CharField(max_length=255)
	type_of_payment_choices = ( 
		('cash', 'Cash'), 
		('mpesa', 'M-Pesa') 
		)
	type_of_payment= models.CharField(choices=type_of_payment_choices, max_length=255)
	createddate = models.DateTimeField(auto_now_add=True)
	modifieddate = models.DateTimeField(auto_now=True)




def check_payment(sender, **kwargs):
	print kwargs
	if kwargs['created']:
		instance=kwargs['instance']
		sp=Order.objects.filter(id=instance.order_id).update(amount_paid=F('amount_paid')+instance.amount_paid)
		print(sp)
post_save.connect(check_payment, sender=Payment)