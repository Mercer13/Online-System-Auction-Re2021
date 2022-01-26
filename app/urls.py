from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("auctions.urls")),

    path('api/v1/account/', include('restaccount.urls')),
    path('api/v1/post/', include('restpost.urls')),
    path('api/v1/profile/', include('restprofile.urls')),
]