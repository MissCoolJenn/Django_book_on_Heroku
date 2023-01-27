from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
    #           ^        ^ ...open in this folder this file
    #           \ like "open"
]
