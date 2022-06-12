from rest_framework import viewsets, status, permissions
from rest_framework.response import Response

from .exceptions import (
    InexistentUserException,
    SameUserException,
)
from .models import Friend
from .serializers import FriendSerializer
from .services import (
    create_friend,
    validate_parameters_friend,
)


class FriendViewSet(viewsets.ModelViewSet):
    """
    Friend
    """
    permission_classes = [permissions.IsAuthenticated]
    queryset = Friend.objects.none()
    serializer_class = FriendSerializer

    def get_serializer_class(self):
        serializer_class = self.serializer_class
        return serializer_class

    def create(self, request, *args, **kwargs):
        """
        Creates a new Friend.

        POST /api/v1/friend/

        @Params:
        - friend_id

        @return Friend Objects
        """
        creator = request.user
        friend_data = request.data

        friend = None
        try:
            friend_id = friend_data['friend_id']

            friend = validate_parameters_friend(
                friend_id=friend_id
            )

            if creator == friend:
                raise SameUserException()

            friend = create_friend(creator, friend)

        except InexistentUserException as e:
            return Response(
                data={'response': f"Usuario {e} inexistente."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        except SameUserException:
            return Response(
                data={'response': "Ambos son el mismo usuario."},
                status=status.HTTP_403_FORBIDDEN,
            )

        except Exception as e:
            err_msg = e.args
            return Response(
                data={'response': f"Error en creación de amigos: {err_msg}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

        if friend is None:
            return Response(
                data={'response': "Hubo un error al crear un nuevo amigo."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        serializer = FriendSerializer(
            friend,
            context={'request': request},
        )

        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED,
        )

    def list(self, request, **kwargs):
        """Get all friends by user"""
        user = request.user

        queryset = None
        if user.is_superuser:
            queryset = Friend.objects.all().order_by("created").reverse()
        else:
            queryset = Friend.objects.filter(creator=user).order_by("created").reverse()

        serializer = FriendSerializer(
            queryset,
            many=True,
            context={'request': request},
        )

        return Response(
            serializer.data,
            status=status.HTTP_200_OK,
        )
