from rest_framework import serializers
from sharebearapi.models.age import Age


class AgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Age
        fields = ["id", "age"]
