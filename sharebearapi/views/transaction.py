from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.utils import timezone
from sharebearapi.models import Transaction, Product
from sharebearapi.serializers import TransactionSerializer


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    def create(self, request):
        product_id = request.data.get("product")
        try:
            product = Product.objects.get(pk=product_id)

            # Check if the user is the owner of the product
            if product.owner == request.user:
                return Response(
                    {"message": "You cannot request your own product."},
                    status=status.HTTP_403_FORBIDDEN,
                )

            # Check if the product is available
            if product.status != "available":
                return Response(
                    {"message": "Product is not available."},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            # Change product status to requested
            product.status = "requested"
            product.save()

            # Create the transaction
            transaction = Transaction.objects.create(
                product_owner=product.owner,  # The owner of the product
                recipient=request.user,  # The logged-in user
                product=product,
                status="pending",  # Set the initial status of the transaction
                request_date=timezone.now(),  # Set the request date to now
                exchange_date=None,  # This can remain null for now
            )

            serializer = self.get_serializer(transaction)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        except Product.DoesNotExist:
            return Response(
                {"message": "Product not found."}, status=status.HTTP_404_NOT_FOUND
            )

    @action(detail=True, methods=["post"])
    def complete_transaction(self, request, pk=None):
        try:
            transaction = self.get_object()

            # Check if the requesting user is the product owner
            if transaction.product.owner != request.user:
                return Response(
                    {
                        "detail": "You do not have permission to complete this transaction."
                    },
                    status=status.HTTP_403_FORBIDDEN,
                )

            transaction.status = "completed"  # Update status to completed
            transaction.exchange_date = timezone.now()  # Set the exchange date

            # Update the product status to shared
            product = transaction.product
            product.status = "shared"
            product.save()

            transaction.save()  # Save the changes

            serializer = self.get_serializer(transaction)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except Transaction.DoesNotExist:
            return Response(
                {"detail": "Transaction not found."}, status=status.HTTP_404_NOT_FOUND
            )

    @action(detail=True, methods=["post"])
    def deny_transaction(self, request, pk=None):
        try:
            transaction = self.get_object()

            # Check if the requesting user is the product owner
            if transaction.product.owner != request.user:
                return Response(
                    {"detail": "You do not have permission to deny this transaction."},
                    status=status.HTTP_403_FORBIDDEN,
                )

            transaction.status = "denied"  # Update status to denied

            # Optionally, update the product status back to available
            product = transaction.product
            product.status = "available"
            product.save()

            transaction.save()  # Save the changes

            serializer = self.get_serializer(transaction)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except Transaction.DoesNotExist:
            return Response(
                {"detail": "Transaction not found."}, status=status.HTTP_404_NOT_FOUND
            )

    @action(detail=True, methods=["post"])
    def cancel_request(self, request, pk=None):
        try:
            transaction = self.get_object()

            # Check if the requesting user is the transaction recipient
            if transaction.recipient != request.user:
                return Response(
                    {"detail": "You do not have permission to cancel this request."},
                    status=status.HTTP_403_FORBIDDEN,
                )

            transaction.status = "canceled"  # Update status to canceled

            # Optionally, update the product status back to available
            product = transaction.product
            product.status = "available"
            product.save()

            transaction.save()  # Save the changes

            serializer = self.get_serializer(transaction)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except Transaction.DoesNotExist:
            return Response(
                {"detail": "Transaction not found."}, status=status.HTTP_404_NOT_FOUND
            )
