<<<<<<< HEAD
# backend/api/admin.py
from django.contrib import admin
from .models import Product, Image, Review

# Inline for Images (allows adding/editing multiple image URLs for a Product)
class ImageInline(admin.TabularInline):  # Use StackedInline if you prefer vertical forms
    model = Image
    extra = 1  # Number of empty rows to show for adding new images (set to 0 to hide)
    fields = ('url',)  # Only show the URL field (keeps it simple)

# Inline for Reviews (allows adding/editing multiple reviews for a Product)
class ReviewInline(admin.TabularInline):  # Use StackedInline for more space on review comments
    model = Review
    extra = 1  # Number of empty rows for new reviews
    fields = ('id', 'author', 'date', 'rating', 'comment')  # All fields from your model
    readonly_fields = ('id',)  # Optional: Make custom review ID read-only if you generate it elsewhere

# Main Product admin (includes the inlines)
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'categoryId', 'price', 'rating')  # Columns in the Product list view
    search_fields = ('name', 'description')  # Search box for name/description
    inlines = [ImageInline, ReviewInline]  # This adds the inline sections to add/edit pages

# Optional: Register Image and Review separately if you want standalone admin pages
@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('url', 'product')
    list_filter = ('product',)  # Filter by product in the Image list

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'product', 'rating', 'date')
    list_filter = ('product', 'rating')  # Filter by product or rating
=======
# backend/api/admin.py
from django.contrib import admin
from .models import Product, Image, Review

# Inline for Images (allows adding/editing multiple image URLs for a Product)
class ImageInline(admin.TabularInline):  # Use StackedInline if you prefer vertical forms
    model = Image
    extra = 1  # Number of empty rows to show for adding new images (set to 0 to hide)
    fields = ('url',)  # Only show the URL field (keeps it simple)

# Inline for Reviews (allows adding/editing multiple reviews for a Product)
class ReviewInline(admin.TabularInline):  # Use StackedInline for more space on review comments
    model = Review
    extra = 1  # Number of empty rows for new reviews
    fields = ('id', 'author', 'date', 'rating', 'comment')  # All fields from your model
    readonly_fields = ('id',)  # Optional: Make custom review ID read-only if you generate it elsewhere

# Main Product admin (includes the inlines)
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'categoryId', 'price', 'rating')  # Columns in the Product list view
    search_fields = ('name', 'description')  # Search box for name/description
    inlines = [ImageInline, ReviewInline]  # This adds the inline sections to add/edit pages

# Optional: Register Image and Review separately if you want standalone admin pages
@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('url', 'product')
    list_filter = ('product',)  # Filter by product in the Image list

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'product', 'rating', 'date')
    list_filter = ('product', 'rating')  # Filter by product or rating
>>>>>>> c8564f1a7c96e97dcf70828858b978ea2200afd3
    search_fields = ('author', 'comment')