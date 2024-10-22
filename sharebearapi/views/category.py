from rest_framework import viewsets, status
from rest_framework.response import Response
from sharebearapi.models import Category
from sharebearapi.serializers import CategorySerializer


class CategoryViewSet(viewsets.ViewSet):
    def list(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
