from rest_framework import viewsets
from sharebearapi.models import Weight
from sharebearapi.serializers import WeightSerializer


class WeightViewSet(viewsets.ModelViewSet):
    queryset = Weight.objects.all()
    serializer_class = WeightSerializer
