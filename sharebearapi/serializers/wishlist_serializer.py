from rest_framework import serializers
from sharebearapi.models import Wishlist


class WishlistSerializer(serializers.ModelSerializer):
    product_id = serializers.IntegerField(write_only=True)
    product = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Wishlist
        fields = ["id", "user", "product", "product_id"]
