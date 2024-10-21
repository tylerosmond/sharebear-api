from django.db import models
from django.contrib.auth.models import User
from .category import Category
from .size import Size
from .age import Age
from .condition import Condition
from .weight import Weight


class Product(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="products")
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    status = models.CharField(max_length=10)
    condition = models.ForeignKey(
        Condition, on_delete=models.DO_NOTHING, related_name="conditions"
    )
    category = models.ForeignKey(
        Category, on_delete=models.DO_NOTHING, related_name="products"
    )
    size = models.ForeignKey(Size, on_delete=models.DO_NOTHING, related_name="sizes")
    min_age = models.ForeignKey(Age, on_delete=models.DO_NOTHING, related_name="ages")
    max_weight = models.ForeignKey(
        Weight, on_delete=models.DO_NOTHING, related_name="weights"
    )
    product_img = models.ImageField(
        upload_to="products",
        height_field=None,
        width_field=None,
        max_length=None,
        null=True,
    )
    created = models.DateTimeField(auto_now_add=True)
