from rest_framework import serializers
from sharebearapi.models.size import Size


class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = ["id", "size"]
