from rest_framework import viewsets, status, permissions
from rest_framework.response import Response

from .exceptions import InexistentCourseException
from .models import Lesson
from .serializers import LessonSerializer
from .services import (
    create_lesson,
    validate_parameters_lesson,
)


class LessonViewSet(viewsets.ModelViewSet):
    """
    Lesson
    """
    permission_classes = [permissions.IsAuthenticated]
    queryset = Lesson.objects.none()
    serializer_class = LessonSerializer

    def get_serializer_class(self):
        serializer_class = self.serializer_class
        return serializer_class

    def create(self, request, *args, **kwargs):
        """
        Creates a new Lesson.

        POST /api/v1/lessons/

        @Params:
        - course_id

        @return Lesson Objects
        """
        user = request.user
        lesson_data = request.data

        lesson = None
        try:
            course_id = lesson_data['course_id']

            course = validate_parameters_lesson(
                course_id=course_id,
            )

            lesson = create_lesson(user, course)

        except InexistentCourseException as e:
            return Response(
                data={'response': f"Curso {e} inexistente."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        except Exception as e:
            err_msg = e.args
            return Response(
                data={'response': f"Error en creación de Lección: {err_msg}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

        if lesson is None:
            return Response(
                data={'response': "Hubo un error al crear una nueva Lección."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        serializer = LessonSerializer(
            lesson,
            context={'request': request},
        )

        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED,
        )

    def list(self, request, **kwargs):
        """Get all lesson by user"""
        user = request.user

        queryset = None
        if user.is_superuser:
            queryset = Lesson.objects.all().order_by("created").reverse()
        else:
            queryset = Lesson.objects.filter(user=user).order_by("created").reverse()

        serializer = LessonSerializer(
            queryset,
            many=True,
            context={'request': request},
        )

        return Response(
            serializer.data,
            status=status.HTTP_200_OK,
        )
