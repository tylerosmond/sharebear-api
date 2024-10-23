from rest_framework import viewsets, status
from rest_framework.response import Response
from sharebearapi.models import Transaction
from sharebearapi.serializers import TransactionSerializer


class TransactionViewSet(viewsets.ViewSet):
    def list(self, request):
        transactions = Transaction.objects.all()
        serializer = TransactionSerializer(transactions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        try:
            transaction = Transaction.objects.get(pk=pk)
            serializer = TransactionSerializer(transaction)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Transaction.DoesNotExist:
            return Response(
                {"message": "Transaction not found"}, status=status.HTTP_404_NOT_FOUND
            )

    def create(self, request):
        serializer = TransactionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        try:
            transaction = Transaction.objects.get(pk=pk)
            transaction.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Transaction.DoesNotExist:
            return Response(
                {"message": "Transaction not found."}, status=status.HTTP_404_NOT_FOUND
            )
