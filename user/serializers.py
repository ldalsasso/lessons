from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from rest_framework import serializers

from lessons.models import Lesson


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email', 'first_name', 'last_name', 'is_superuser')
        extra_kwargs = {'password': {'write_only': True}}
        read_only_fields = ('id', 'is_superuser')

    def create(self, validated_data):
        user = get_user_model().objects.create_user(**validated_data)
        return user

    def update(self, instance, validated_data):
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)
        return super(UserSerializer, self).update(instance, validated_data)


class UserAndLessonSerializer(serializers.ModelSerializer):

    lessons = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'lessons')
        read_only_fields = ('id',)

    def get_lessons(self, obj):
        from lessons.serializers import LessonSimpleSerializer

        lessons = Lesson.objects.filter(user=obj)

        return LessonSimpleSerializer(
            lessons,
            source='user__lesson_user',
            many=True
        ).data

