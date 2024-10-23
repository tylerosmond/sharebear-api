from rest_framework import viewsets
from sharebearapi.models import Condition
from sharebearapi.serializers import ConditionSerializer


class ConditionViewSet(viewsets.ModelViewSet):
    queryset = Condition.objects.all()
    serializer_class = ConditionSerializer
