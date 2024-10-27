from rest_framework import serializers
from sharebearapi.models.product import Product
from sharebearapi.models.category import Category
from sharebearapi.models.size import Size
from sharebearapi.models.age import Age
from sharebearapi.models.weight import Weight
from sharebearapi.models.condition import Condition
from .age_serializer import AgeSerializer
from .category_serializer import CategorySerializer
from .condition_serializer import ConditionSerializer
from .size_serializer import SizeSerializer
from .weight_serializer import WeightSerializer
from ..views.users import UserSerializer


class ProductSerializer(serializers.ModelSerializer):
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
    owner = UserSerializer(read_only=True)

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
        read_only_fields = ["owner", "status", "created"]

    def create(self, validated_data):
        validated_data["owner"] = self.context["request"].user
        validated_data["status"] = "available"
        return super().create(validated_data)

    def to_representation(self, instance):
        """Customize the output representation to include nested serializers."""
        representation = super().to_representation(instance)
        representation["category"] = CategorySerializer(instance.category).data
        representation["condition"] = ConditionSerializer(instance.condition).data
        if instance.size:
            representation["size"] = SizeSerializer(instance.size).data
        if instance.min_age:
            representation["min_age"] = AgeSerializer(instance.min_age).data
        if instance.max_weight:
            representation["max_weight"] = WeightSerializer(instance.max_weight).data
        return representation
