from django.urls import path
from .. import views

product_urlpattern = [
    path('products/', views.get_products, name='products'),
    path('products/<str:pk>', views.get_product, name='product'),
]
