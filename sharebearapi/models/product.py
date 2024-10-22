from django.db import models
from django.contrib.auth.models import User
from .category import Category
from .size import Size
from .age import Age
from .condition import Condition
from .weight import Weight


class Product(models.Model):
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="products", verbose_name="Owner"
    )
    name = models.CharField(max_length=200, verbose_name="Product Name")
    description = models.CharField(max_length=200, verbose_name="Product Description")
    status = models.CharField(
        max_length=10,
        choices=[
            ("available", "Available"),
            ("requested", "Requested"),
            ("shared", "Shared"),
            ("inactive", "Inactive"),
        ],
        verbose_name="Availability Status",
    )
    condition = models.ForeignKey(
        Condition,
        on_delete=models.DO_NOTHING,
        related_name="products",
        verbose_name="Condition",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.DO_NOTHING,
        related_name="products",
        verbose_name="Category",
    )
    size = models.ForeignKey(
        Size,
        on_delete=models.DO_NOTHING,
        related_name="products",
        null=True,
        verbose_name="Size",
    )
    min_age = models.ForeignKey(
        Age,
        on_delete=models.DO_NOTHING,
        related_name="products",
        null=True,
        verbose_name="Minimum Age",
    )
    max_weight = models.ForeignKey(
        Weight,
        on_delete=models.DO_NOTHING,
        related_name="products",
        null=True,
        verbose_name="Maximum Weight",
    )
    product_img = models.CharField(max_length=200, null=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Date Created")

    def __str__(self):
        return f"{self.name} by {self.owner.username}"
