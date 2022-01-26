from rest_framework import serializers
from rest_framework.serializers import (
	ModelSerializer,
)
from auctions.models import Listing, Category


class listSerializer(ModelSerializer):
	class Meta:
		model = Listing
		fields = [
			'id',
			'title',
			'description',
			'category',
			'image',
			'bid',
			'active',
			'created'
		]


class addSerializer(ModelSerializer):
	class Meta:
		model = Listing
		fields = [
			'id',
			'category',
			'title',
			'description',
			'image',
			'bid',
			'active'
		]
		
class showSerializer(ModelSerializer):
	class Meta:
		model = Listing
		fields = [
			'id',
			'title',
			'description',
			'category',
			'bid',
			'image'
			
		]

class listCategorySerializer(ModelSerializer):
	class Meta:
		model = Category
		fields = [
			'id',
			'catname',
		]

