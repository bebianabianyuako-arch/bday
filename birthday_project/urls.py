# File: birthday_project/urls.py
from django.urls import path
from wishes.views import home

# Tambahkan import untuk serving static files
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name='home'),
]

# Hanya tambahkan ini jika DEBUG = True (Mode Pengembangan)
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])

# PENTING: Untuk memastikan semua static files terdeteksi
# kita gunakan STATICFILES_DIRS sebagai root dokumen.