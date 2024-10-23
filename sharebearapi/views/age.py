from rest_framework import viewsets
from sharebearapi.models import Age
from sharebearapi.serializers import AgeSerializer


class AgeViewSet(viewsets.ModelViewSet):
    queryset = Age.objects.all()
    serializer_class = AgeSerializer
