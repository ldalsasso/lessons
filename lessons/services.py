from courses.services import get_course
from user.services import get_user

from .exceptions import InexistentCourseException
from .models import Lesson


def validate_parameters_lesson(course_id):
    """
    Validate parameters of lesson.
    Return:
        - course object
    """
    course = get_course(course_id)
    if not course:
        raise InexistentCourseException(f"ID#{course_id}")

    return course


def create_lesson(user, course):
    """Create a new lesson"""
    return Lesson.objects.create(
        user=user,
        course=course,
    )
