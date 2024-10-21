from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Weight(models.Model):
    weight = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(150)]
    )
