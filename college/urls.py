from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import urls
from hostels.views import sign_up

urlpatterns = [
    path('hostels/',include('hostels.urls')),
    path('admin/', admin.site.urls),
    path('',include(urls)),
    path('sign-up/',sign_up),
]
