from django.contrib.contenttypes.models import ContentType
from rest_framework import serializers
from .models import Merchant
from django.db.models import Q

class MerchantSerializer(serializers.ModelSerializer):
	"""docstring for MerchantSerializer"""
	class Meta:
		
			model = Merchant
			fields = ('id', 'merchantname', 'krapin', 'phonenumber', 'email')
			

#user validation
	def validate(self, data):
		merchant_obj = None
		email = data.get("email", None)
		storename = data.get("storename",None)
		password = data["password"]

		#there has to be a username or email
		if not email and not storename:
			raise ValidationError ("A storename or email is required to login")

		#performing set query search
		merchant = Merchant.objects.filter(
					Q(email=email) |
					Q(storename=storename)
				).distinct()
		if merchant.exists() and merchant.count() ==1:
				merchant = merchant.first()
		else:
				raise ValidationError("This storename/email is not valid,")
		#password has to be correct based on the user/email selected
		if merchant_obj:
			if not merchant_obj.check_password(password):
					raise ValidationError("Incorrect credentials please try again")



		return data
			