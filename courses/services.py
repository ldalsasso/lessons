from .models import Course


def get_course(course_id):
    """ get course by id"""
    course = None
    try:
        return Course.objects.get(id=course_id)
    except Exception:
        return course
