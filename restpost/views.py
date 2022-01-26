from django.shortcuts import render

from rest_framework.views import APIView
from django.http import HttpResponse
from django.http import JsonResponse

from .serializers import (listSerializer, showSerializer, listCategorySerializer, addSerializer)

	

from rest_framework.generics import (CreateAPIView, RetrieveUpdateAPIView, DestroyAPIView, ListAPIView, RetrieveAPIView)
from rest_framework.response import Response

from auctions.models import Listing, Category


from rest_framework.permissions import (
	IsAuthenticated,
	)

from rest_framework.authentication import TokenAuthentication
from rest_framework.authentication import SessionAuthentication
# Create your views here.

class PostListAPIView(ListAPIView):
	serializer_class = listSerializer
	
	queryset = Listing.objects.all()

class ShowPost(RetrieveAPIView):
	queryset = Listing.objects.all()
	serializer_class = showSerializer
	lookup_field = 'id'

class CategoryAllAPIView(ListAPIView):
	serializer_class = listCategorySerializer
	queryset = Category.objects.all()

class CategoryIdAPIView(ListAPIView):
	serializer_class = listSerializer

	def get_queryset(self):
		return Listing.objects.filter(category=self.kwargs['id'])

class AddPost(CreateAPIView):
	authentication_classes = (TokenAuthentication, SessionAuthentication)
	permission_classes = (IsAuthenticated,)
	serializer_class = addSerializer
	queryset = Listing.objects.all()

	def perform_create(self, serializer):
		serializer.save(user_id=self.request.user)