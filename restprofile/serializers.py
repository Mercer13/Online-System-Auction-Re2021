from rest_framework import serializers
from rest_framework.serializers import (
	ModelSerializer,
)
from auctions.models import Listing, Category

class listUserSerializer(ModelSerializer):
	class Meta:
		model = Listing
		fields = [
			'id',
			'title',
			'description',
		]


class deleteSerializer(ModelSerializer):
	class Meta:
		model = Listing
		fields = [
			'id',
		]


class updateSerializer(ModelSerializer):
	class Meta:
		model = Listing
		fields = [
			'category',
			'title',
			'description',
		]