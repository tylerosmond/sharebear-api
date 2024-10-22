from django.db import models
from django.contrib.auth.models import User
from .product import Product


class Transaction(models.Model):
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="transactions_as_owner"
    )
    recipient = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="transactions_as_recipient"
    )
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="transactions"
    )
    exchange_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20,
        default="pending",
        choices=[
            ("pending", "Pending"),
            ("completed", "Completed"),
            ("canceled", "Canceled"),
        ],
    )

    class Meta:
        unique_together = ("owner", "recipient", "product")

    def __str__(self):
        return f"{self.product.name} exchanged from {self.owner.username} to {self.recipient.username} on {self.exchange_date}"
