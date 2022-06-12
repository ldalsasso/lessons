from rest_framework import serializers

from user.serializers import (
    UserAndLessonSerializer,
    UserSerializer,
)

from .models import Friend


class FriendSerializer(serializers.ModelSerializer):

    creator = UserSerializer(read_only=True)
    friend_user = UserAndLessonSerializer(read_only=True)

    class Meta:
        model = Friend
        fields = ('creator', 'friend_user', 'created', 'updated')
        read_only_fields = ('created', 'updated')
