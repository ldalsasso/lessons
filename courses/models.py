from django.db import models

from common.models import BaseDatedModel


class Course(BaseDatedModel):
    """Course model"""

    name = models.CharField(
        unique=True,
        db_index=True,
        max_length=100,
    )

    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"

    def __str__(self):
        return f"Curso ID#{self.id} - {self.name}"
