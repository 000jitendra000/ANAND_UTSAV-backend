<<<<<<< HEAD
from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('data/', views.getData),
    path('products/', views.product_list, name='product-list'),
]
=======
from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('data/', views.getData),
    path('products/', views.product_list, name='product-list'),
]
>>>>>>> c8564f1a7c96e97dcf70828858b978ea2200afd3
