from rest_framework import serializers
from sharebearapi.models.product import Product
from sharebearapi.serializers.category_serializer import CategorySerializer
from sharebearapi.serializers.size_serializer import SizeSerializer
from sharebearapi.serializers.age_serializer import AgeSerializer
from sharebearapi.serializers.weight_serializer import WeightSerializer
from sharebearapi.serializers.condition_serializer import ConditionSerializer


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    size = SizeSerializer()
    min_age = AgeSerializer()
    max_weight = WeightSerializer()
    condition = ConditionSerializer()

    class Meta:
        model = Product
        fields = [
            "id",
            "owner",
            "name",
            "description",
            "status",
            "condition",
            "category",
            "size",
            "min_age",
            "max_weight",
            "product_img",
            "created",
        ]
