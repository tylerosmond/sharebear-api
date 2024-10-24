from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from sharebearapi.models import Wishlist, Product
from sharebearapi.serializers import WishlistSerializer


class WishlistViewSet(viewsets.ModelViewSet):
    queryset = Wishlist.objects.all()
    serializer_class = WishlistSerializer

    def create(self, request):
        product_id = request.data.get("product_id")
        try:
            # Check if product exists
            product = Product.objects.get(pk=product_id)

            # Check if the logged-in user is trying to add their own product to the wishlist
            if product.owner == request.user:
                return Response(
                    {"message": "You cannot add your own product to the wishlist."},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            # Check if the product is already in the user's wishlist
            if Wishlist.objects.filter(user=request.user, product=product).exists():
                return Response(
                    {"message": "This product is already in your wishlist."},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            # Create the wishlist entry
            wishlist_item = Wishlist.objects.create(user=request.user, product=product)

            serializer = self.get_serializer(wishlist_item)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        except Product.DoesNotExist:
            return Response(
                {"message": "Product not found."}, status=status.HTTP_404_NOT_FOUND
            )

    @action(detail=True, methods=["delete"])
    def remove_from_wishlist(self, request, pk=None):
        # Custom action to remove a product from the wishlist
        try:
            wishlist_item = Wishlist.objects.get(pk=pk, user=request.user)
            wishlist_item.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Wishlist.DoesNotExist:
            return Response(
                {"message": "Wishlist item not found."},
                status=status.HTTP_404_NOT_FOUND,
            )
