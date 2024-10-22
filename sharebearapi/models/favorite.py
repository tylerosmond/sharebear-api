from django.db import models
from django.contrib.auth.models import User

# Stretch Goal


class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    favorite_sharer = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, related_name="favorited_user"
    )

    class Meta:
        unique_together = ("user", "favorite_sharer")  # Prevents duplicate favorites

    def __str__(self):
        return f"{self.user.username} favorites {self.favorite_sharer.username}"
