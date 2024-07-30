from dataclasses import field
from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = "__all__" #to get all the fields

        # fields = ('name', 'price' ) #to show some specific field


        
