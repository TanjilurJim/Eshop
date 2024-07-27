from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from . models import Product

# Create your views here.
@api_view(['GET'])
def get_products(request):

    products = Product.objects.all() #it will get all the objects from db

    print(products )

    return Response({"Hello": 'hello'})

