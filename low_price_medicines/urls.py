# low_price_medicines/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('medicines.urls')),  # Include medicine app URLs
]
