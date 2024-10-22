from django.db import models
from django.contrib.auth.models import User
from .product import Product


class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="wishlistitem",
        verbose_name="Wishlist Item",
    )

    def __str__(self):
        return f"{self.user.username} has added {self.product.name} to Wishlist"

    class Meta:
        unique_together = ("user", "product")
