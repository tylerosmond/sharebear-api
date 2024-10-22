from rest_framework import viewsets, status
from rest_framework.response import Response
from sharebearapi.models import Size
from sharebearapi.serializers import SizeSerializer


class SizeViewSet(viewsets.ViewSet):
    def list(self, request):
        sizes = Size.objects.all()
        serializer = SizeSerializer(sizes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
