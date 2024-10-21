from django.db import models
from django.contrib.auth.models import User
from .product import Product


class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    product = models.ForeignKey(
        Product, on_delete=models.DO_NOTHING, related_name="wishlistitem"
    )
