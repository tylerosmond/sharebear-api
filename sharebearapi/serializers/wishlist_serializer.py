from rest_framework import serializers
from sharebearapi.models.wishlist import Wishlist
from sharebearapi.serializers.product_serializer import ProductSerializer


class WishlistSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = Wishlist
        fields = ["id", "user", "product"]
