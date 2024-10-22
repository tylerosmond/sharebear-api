from rest_framework import viewsets, status
from rest_framework.response import Response
from sharebearapi.models import Wishlist
from sharebearapi.serializers import WishlistSerializer


class WishlistViewSet(viewsets.ViewSet):
    def list(self, request):
        wishlist = Wishlist.objects.filter(user=request.user)
        serializer = WishlistSerializer(wishlist, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = WishlistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        try:
            wishlist_item = Wishlist.objects.get(pk=pk, user=request.user)
            wishlist_item.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Wishlist.DoesNotExist:
            return Response(
                {"message": "Wishlist item not found"}, status=status.HTTP_404_NOT_FOUND
            )
