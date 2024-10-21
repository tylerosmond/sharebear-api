from django.db import models
from django.contrib.auth.models import User
from .product import Product


class Transaction(models.Model):
    owner = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    recipient = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    product = models.ForeignKey(
        Product, on_delete=models.DO_NOTHING, related_name="shareitem"
    )
    exchange_date = models.DateTimeField(auto_now_add=True)
