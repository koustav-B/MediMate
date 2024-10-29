# medicines/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page for searching
    path('search/', views.search, name='search'),  # Search results
]
