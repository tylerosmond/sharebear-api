from rest_framework import serializers
from sharebearapi.models.transaction import Transaction
from sharebearapi.serializers.product_serializer import ProductSerializer


class TransactionSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = Transaction
        fields = ["id", "owner", "recipient", "product", "status", "exchange_date"]
