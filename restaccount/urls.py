from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken import views as authviews
from . import views

urlpatterns = [
    path('users/', views.UserList.as_view()),
    path('register/', views.Register.as_view()),
    path('api-token-auth/', authviews.obtain_auth_token, name='api-token-auth'),
    path('users/<int:pk>/', views.UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)