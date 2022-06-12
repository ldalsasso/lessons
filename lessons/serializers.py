from rest_framework import serializers

from courses.serializers import CourseSerializer
from user.serializers import UserSerializer

from .models import Lesson


class LessonSerializer(serializers.ModelSerializer):

    user = UserSerializer(read_only=True)
    course = CourseSerializer(read_only=True)

    class Meta:
        model = Lesson
        fields = ('id', 'user', 'course', 'finalized_date', 'created', 'updated')
        read_only_fields = ('id', 'created', 'updated')


class LessonSimpleSerializer(serializers.ModelSerializer):

    course = serializers.SerializerMethodField()

    class Meta:
        model = Lesson
        fields = ('course', 'created')

    def get_course(self, obj):
        return obj.course.name
