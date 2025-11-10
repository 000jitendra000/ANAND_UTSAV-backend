from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('data/', views.getData),
    path('products/', views.product_list, name='product-list'),
]
