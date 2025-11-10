# backend/api/serializers.py

from rest_framework import serializers
# Make sure to import all your models
from .models import Product, Image, Review 


# 1. Define the ReviewSerializer
# This must be defined first because it's used inside the ProductSerializer.
class ReviewSerializer(serializers.ModelSerializer):
    # Your JSON uses rating as a number (5, 4), and date as a string ("YYYY-MM-DD")
    # Django Rest Framework will handle this mapping automatically.
    class Meta:
        model = Review
        fields = ['id', 'author', 'date', 'rating', 'comment']


# 2. Define the ImageSerializer
class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['url']


# 3. Define the ProductSerializer
class ProductSerializer(serializers.ModelSerializer):
    # Use ImageSerializer(many=True) if you want the full image object data (less efficient)
    # OR keep the more efficient SlugRelatedField you had to only return the URL.
    # To match your desired output (an array of URL strings), use SlugRelatedField:
    images = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='url'
    )
    
    # Use the defined ReviewSerializer to nest the full review objects.
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = [
            'id', 
            'name', 
            'categoryId', 
            'price', 
            'priceInfo', 
            'rating', 
            'description', 
            'images', # This will use the SlugRelatedField (array of URLs)
            'reviews' # This will use the ReviewSerializer (array of objects)
        ]