from rest_framework import serializers
from .models import MyUser
from django.contrib.auth import get_user_model

class UserSerializer(serializers.ModelSerializer):
	#age = serializers.DateField(format="%d-%m-%Y", input_formats=['%d-%m-%Y', 'iso-8601'])

	class Meta:
			model = MyUser
			fields = '__all__'
		
		   # model = User
		   # fields = ('userid', 'username', 'location', 'phonenumber', 'email', 'password', 'age', 'location')



	# def create(self, validated_data):
	#     # print(validated_data)
	#     password = validated_data.pop('password', None)
	#     instance = self.Meta.model(**validated_data)
	#     if password is not None:
	#         instance.set_password(password)
	#     instance.save()
	#     return instance

	def update(self, instance, validated_data):
	    for attr, value in validated_data.items():
	        if attr == 'password':
	            instance.set_password(value)
	        else:
	            setattr(instance, attr, value)
	    instance.save()
	    return instance