from django.db import models
from django.contrib.auth.models import User

# Stretch Goal


class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    favorite_user = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, related_name="favorited_user"
    )
