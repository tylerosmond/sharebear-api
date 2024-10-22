from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Weight(models.Model):
    weight = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(150)],
        verbose_name="Weight (lbs)",
    )

    def __str__(self):
        return f"{self.weight} lbs"
