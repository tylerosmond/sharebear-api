from rest_framework import serializers
from sharebearapi.models.weight import Weight


class WeightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weight
        fields = ["id", "weight"]
