from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.serializers import (
	ModelSerializer,
	ValidationError,
	EmailField,
)
 

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

class RegisterSerializer(ModelSerializer):
	email = EmailField(label='Email adress')
	class Meta:
		model = User
		fields = [
			'id',
			'username',
			'password',
			'email',
		]
	extra_kwargs = {"password":
					{"write_only":True},
					"id":
					{"read_only":True}
					}

	def validate(self, data):
		return data

	def validate_email(self, value):
		email = value
		user_qs = User.objects.filter(email=email)
		if user_qs.exists():
			raise ValidationError("Email alredy registred")
		return value


	def create(self, validated_data):
		username = validated_data['username']
		password = validated_data['password']
		email = validated_data['email']
		user_obj = User(
			username = username,
			email = email,
		)
		user_obj.set_password(password)
		user_obj.save()
		return user_obj