<<<<<<< HEAD
# backend/api/management/commands/import_products.py
import json
from django.core.management.base import BaseCommand
from django.utils.dateparse import parse_date
from api.models import Product, Image, Review

class Command(BaseCommand):
    help = 'Import products from a JSON file'

    def add_arguments(self, parser):
        parser.add_argument('json_file', type=str, help='Path to the JSON file')

    def handle(self, *args, **kwargs):
        json_file = kwargs['json_file']
        try:
            with open(json_file, 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            self.stderr.write(f"Error: File {json_file} not found")
            return
        except json.JSONDecodeError:
            self.stderr.write(f"Error: Invalid JSON format in {json_file}")
            return

        # Handle multiple products if the JSON is a list
        if isinstance(data, list):
            products_data = data
        else:
            products_data = [data]

        for product_data in products_data:
            try:
                # Create or update Product
                product, created = Product.objects.update_or_create(
                    id=product_data['id'],
                    defaults={
                        'name': product_data['name'],
                        'categoryId': product_data['categoryId'],
                        'price': product_data['price'],
                        'priceInfo': product_data.get('priceInfo', ''),
                        'rating': product_data.get('rating', 0.0),
                        'description': product_data.get('description', '')
                    }
                )

                # Clear existing images and reviews to avoid duplicates
                product.images.all().delete()
                product.reviews.all().delete()

                # Create Images
                for url in product_data.get('images', []):
                    Image.objects.create(product=product, url=url)

                # Create Reviews
                for review_data in product_data.get('reviews', []):
                    Review.objects.create(
                        id=review_data['id'],
                        product=product,
                        author=review_data['author'],
                        date=parse_date(review_data['date']),
                        rating=review_data['rating'],
                        comment=review_data['comment']
                    )

                self.stdout.write(self.style.SUCCESS(f"Successfully imported product {product.name} ({product.id})"))

            except KeyError as e:
                self.stderr.write(f"Error: Missing key {e} in product data")
            except Exception as e:
                self.stderr.write(f"Error importing product {product_data.get('id', 'unknown')}: {str(e)}")
=======
# backend/api/management/commands/import_products.py
import json
from django.core.management.base import BaseCommand
from django.utils.dateparse import parse_date
from api.models import Product, Image, Review

class Command(BaseCommand):
    help = 'Import products from a JSON file'

    def add_arguments(self, parser):
        parser.add_argument('json_file', type=str, help='Path to the JSON file')

    def handle(self, *args, **kwargs):
        json_file = kwargs['json_file']
        try:
            with open(json_file, 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            self.stderr.write(f"Error: File {json_file} not found")
            return
        except json.JSONDecodeError:
            self.stderr.write(f"Error: Invalid JSON format in {json_file}")
            return

        # Handle multiple products if the JSON is a list
        if isinstance(data, list):
            products_data = data
        else:
            products_data = [data]

        for product_data in products_data:
            try:
                # Create or update Product
                product, created = Product.objects.update_or_create(
                    id=product_data['id'],
                    defaults={
                        'name': product_data['name'],
                        'categoryId': product_data['categoryId'],
                        'price': product_data['price'],
                        'priceInfo': product_data.get('priceInfo', ''),
                        'rating': product_data.get('rating', 0.0),
                        'description': product_data.get('description', '')
                    }
                )

                # Clear existing images and reviews to avoid duplicates
                product.images.all().delete()
                product.reviews.all().delete()

                # Create Images
                for url in product_data.get('images', []):
                    Image.objects.create(product=product, url=url)

                # Create Reviews
                for review_data in product_data.get('reviews', []):
                    Review.objects.create(
                        id=review_data['id'],
                        product=product,
                        author=review_data['author'],
                        date=parse_date(review_data['date']),
                        rating=review_data['rating'],
                        comment=review_data['comment']
                    )

                self.stdout.write(self.style.SUCCESS(f"Successfully imported product {product.name} ({product.id})"))

            except KeyError as e:
                self.stderr.write(f"Error: Missing key {e} in product data")
            except Exception as e:
                self.stderr.write(f"Error importing product {product_data.get('id', 'unknown')}: {str(e)}")
>>>>>>> c8564f1a7c96e97dcf70828858b978ea2200afd3
