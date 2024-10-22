from django.db import models


class Condition(models.Model):
    condition = models.CharField(max_length=50)

    def __str__(self):
        return str(self.condition)
