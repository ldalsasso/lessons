from django.contrib.auth.models import User
from rest_framework import viewsets

from rest_framework.permissions import IsAuthenticated

from .permissions import PermissionForUser
from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer

    def get_permissions(self):
        permission_classes = None
        if self.action == 'list' or self.action == 'retrieve':
            permission_classes = (IsAuthenticated, PermissionForUser)
        else:
            permission_classes = [PermissionForUser]
        return [permission() for permission in permission_classes]
