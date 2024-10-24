# from rest_framework import serializers
# from sharebearapi.models.transaction import Transaction
# from sharebearapi.serializers.product_serializer import ProductSerializer


# class TransactionSerializer(serializers.ModelSerializer):
#     product = ProductSerializer()

#     class Meta:
#         model = Transaction
#         fields = ["id", "owner", "recipient", "product", "status", "exchange_date"]
from rest_framework import serializers
from sharebearapi.models.transaction import Transaction
from sharebearapi.models.product import Product


class TransactionSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())

    class Meta:
        model = Transaction
        fields = [
            "id",
            "product_owner",
            "recipient",
            "product",
            "status",
            "request_date",
            "exchange_date",
        ]
        read_only_fields = ["exchange_date"]
