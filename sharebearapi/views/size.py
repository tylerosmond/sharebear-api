from rest_framework import viewsets
from sharebearapi.models import Size
from sharebearapi.serializers import SizeSerializer


class SizeViewSet(viewsets.ModelViewSet):
    queryset = Size.objects.all()
    serializer_class = SizeSerializer
