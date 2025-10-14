# backend/api/models.py
from django.db import models

class Product(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    categoryId = models.IntegerField()
    price = models.IntegerField()
    priceInfo = models.CharField(max_length=255, blank=True)
    rating = models.FloatField(default=0.0)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name} ({self.id})"

class Image(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    url = models.URLField()

    def __str__(self):
        return f"Image for {self.product.name}: {self.url}"

class Review(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    product = models.ForeignKey(Product, related_name='reviews', on_delete=models.CASCADE)
    author = models.CharField(max_length=100)
    date = models.DateField()
    rating = models.FloatField()
    comment = models.TextField()

    def __str__(self):
        return f"Review {self.id} for {self.product.name} by {self.author}"