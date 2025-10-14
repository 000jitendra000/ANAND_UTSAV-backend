# backend/api/serializers.py
class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['url']

class ProductSerializer(serializers.ModelSerializer):
    images = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='url'
    )
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'categoryId', 'price', 'priceInfo', 'rating', 'description', 'images', 'reviews']

# backend/api/serializers.py
class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['url']

class ProductSerializer(serializers.ModelSerializer):
    images = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='url'
    )
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'categoryId', 'price', 'priceInfo', 'rating', 'description', 'images', 'reviews']
