from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Age(models.Model):
    age = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(18)])

    def __str__(self):
        return f"{self.age}+"
