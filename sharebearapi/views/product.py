from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from sharebearapi.models import Product
from sharebearapi.serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    # Optional custom action for requesting a share of a product
    @action(detail=True, methods=["post"])
    def request_share(self, request, pk=None):
        # Custom logic for requesting a share of a product
        return Response({"message": "Custom share logic not yet implemented."})
