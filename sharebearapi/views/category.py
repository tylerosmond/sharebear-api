from rest_framework import viewsets
from sharebearapi.models import Category
from sharebearapi.serializers import CategorySerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
