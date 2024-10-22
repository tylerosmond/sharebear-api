from rest_framework import viewsets, status
from rest_framework.response import Response
from sharebearapi.models import Condition
from sharebearapi.serializers import ConditionSerializer


class ConditionViewSet(viewsets.ViewSet):
    def list(self, request):
        conditions = Condition.objects.all()
        serializer = ConditionSerializer(conditions, many=True)
        return Response(serializer.data, status.HTTP_200_OK)
