from rest_framework import generics
from . import serializers
from django.contrib.auth.models import User
from rest_framework.permissions import (
	AllowAny,
	)

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer

class Register(generics.CreateAPIView):
	permission_classes = (AllowAny,)

	serializer_class = serializers.RegisterSerializer
	queryset = User.objects.all()