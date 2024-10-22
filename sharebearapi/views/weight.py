from rest_framework import viewsets, status
from rest_framework.response import Response
from sharebearapi.models import Weight
from sharebearapi.serializers import WeightSerializer


class WeightViewSet(viewsets.ViewSet):
    def list(self, request):
        weights = Weight.objects.all()
        serializer = WeightSerializer(weights, many=True)
        return Response(serializer.data, status.HTTP_200_OK)
