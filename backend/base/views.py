from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .products import products
# Create your views here.

@api_view(['GET'])
def get_routes(request):
    routes = [
        '/api/products/',
        '/api/products/create/',

        '/api/products/upload/',

        '/api/products/<id>/reviews/',

        '/api/products/top/',
        '/api/products/<id>/',

        '/api/products/delete/<id>/',
        '/api/products/update/<id>/',

    ]
    return Response(routes)
    

@api_view(['GET'])
def get_products(request):
    return Response(products)


@api_view(['GET'])
def get_product(request, pk):
    product = None
    for i in products:
        if i['_id'] == pk:
            product = i
            return Response(product, status=status.HTTP_200_OK)
    return Response({'message': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)