# File: birthday_project/urls.py

from django.urls import path
# Hapus baris di bawah ini
# from django.contrib import admin 
from wishes.views import home

urlpatterns = [
    # Hapus atau komentari baris di bawah ini
    # path('admin/', admin.site.urls), 
    path('', home, name='home'),
]