from django.contrib.auth.models import User
from django.db import models

from common.models import BaseDatedModel

from courses.models import Course


class Friend(BaseDatedModel):
    """Friend model"""

    creator = models.ForeignKey(
        User,
        verbose_name="Creator",
        related_name='friend_creator',
        on_delete=models.PROTECT,
        db_index=True,
    )

    friend_user = models.ForeignKey(
        User,
        verbose_name="Friend",
        related_name='friend_friend_user',
        on_delete=models.PROTECT,
        db_index=True,
    )

    class Meta:
        unique_together = (('creator', 'friend_user'), )
        verbose_name = "Amigo"
        verbose_name_plural = "Amigos"

    def __str__(self):
        return f"Friend - Creator:{self.creator} - Friend:{self.friend_user}"
