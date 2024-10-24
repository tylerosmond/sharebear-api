# from rest_framework import serializers
# from sharebearapi.models.product import Product
# from .category_serializer import CategorySerializer
# from .size_serializer import SizeSerializer
# from .age_serializer import AgeSerializer
# from .weight_serializer import WeightSerializer
# from .condition_serializer import ConditionSerializer


# class ProductSerializer(serializers.ModelSerializer):
#     category = CategorySerializer()
#     size = SizeSerializer()
#     min_age = AgeSerializer()
#     max_weight = WeightSerializer()
#     condition = ConditionSerializer()

#     class Meta:
#         model = Product
#         fields = [
#             "id",
#             "owner",
#             "name",
#             "description",
#             "status",
#             "condition",
#             "category",
#             "size",
#             "min_age",
#             "max_weight",
#             "product_img",
#             "created",
#         ]

from rest_framework import serializers
from sharebearapi.models.product import Product
from sharebearapi.models.category import Category
from sharebearapi.models.size import Size
from sharebearapi.models.age import Age
from sharebearapi.models.weight import Weight
from sharebearapi.models.condition import Condition


class ProductSerializer(serializers.ModelSerializer):
    # Use PrimaryKeyRelatedField to accept just the IDs of related models
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    condition = serializers.PrimaryKeyRelatedField(queryset=Condition.objects.all())
    size = serializers.PrimaryKeyRelatedField(
        queryset=Size.objects.all(), allow_null=True, required=False
    )
    min_age = serializers.PrimaryKeyRelatedField(
        queryset=Age.objects.all(), allow_null=True, required=False
    )
    max_weight = serializers.PrimaryKeyRelatedField(
        queryset=Weight.objects.all(), allow_null=True, required=False
    )

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
        # Owner and status should be read-only
        read_only_fields = ["owner", "status", "created"]

    def create(self, validated_data):
        # Automatically set the owner to the current user and status to 'available'
        validated_data["owner"] = self.context["request"].user
        validated_data["status"] = "available"
        return super().create(validated_data)
