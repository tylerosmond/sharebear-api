from rest_framework import viewsets, status
from rest_framework.response import Response
from sharebearapi.models import Age
from sharebearapi.serializers import AgeSerializer


class AgeViewSet(viewsets.ViewSet):
    def list(self, request):
        ages = Age.objects.all()
        serializer = AgeSerializer(ages, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
