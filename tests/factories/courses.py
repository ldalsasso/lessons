from factory import LazyFunction
from factory.django import DjangoModelFactory
import faker

from courses.models import Course

from .utils import (
    COURSES_CHOICES,
    get_random_choice_from_choices,
)

faker = faker.Factory.create()


class CourseFactory(DjangoModelFactory):

    class Meta:
        model = Course

    name = LazyFunction(
        lambda: get_random_choice_from_choices(
            COURSES_CHOICES
        )
    )
