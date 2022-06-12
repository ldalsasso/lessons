from django.contrib.auth.models import User
from django.db import models

from common.models import BaseDatedModel

from courses.models import Course


class Lesson(BaseDatedModel):
    """Lesson model"""

    user = models.ForeignKey(
        User,
        verbose_name="Usuario",
        related_name='lesson_user',
        on_delete=models.PROTECT,
        db_index=True,
    )

    course = models.ForeignKey(
        Course,
        verbose_name="Course",
        related_name='lesson_course',
        on_delete=models.PROTECT,
        db_index=True,
    )

    finalized_date = models.DateTimeField(
        verbose_name="Fecha Finalización",
        null=True, blank=True,
    )

    class Meta:
        verbose_name = "Lección"
        verbose_name_plural = "Lecciones"

    def __str__(self):
        return f"Lesson ID#{self.id} - User:{self.user} - Course:{self.course}"
