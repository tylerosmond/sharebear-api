from django.db import models
from django.contrib.auth.models import User
from .product import Product


class Transaction(models.Model):
    product_owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="transactions_as_owner"
    )
    recipient = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="transactions_as_recipient"
    )
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="transactions"
    )
    request_date = models.DateTimeField(auto_now_add=True)
    exchange_date = models.DateTimeField(null=True, blank=True)
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
        unique_together = ("product_owner", "recipient", "product")

    def __str__(self):
        return f"{self.product.name} exchanged from {self.owner.username} to {self.recipient.username} on {self.exchange_date}"
