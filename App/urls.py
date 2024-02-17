from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.product_list, name='product_list'),
    path('products_dummy/', views.products_dummy, name='products-dummy'),
]
