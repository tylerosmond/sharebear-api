from rest_framework import serializers
from sharebearapi.models.condition import Condition


class ConditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Condition
        fields = ["id", "condition"]
