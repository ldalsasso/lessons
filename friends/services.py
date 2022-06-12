from user.services import get_user

from .exceptions import InexistentUserException
from .models import Friend


def validate_parameters_friend(friend_id):
    """
    Validate parameters of friends.
    Return:
        - friend
    """
    friend = get_user(friend_id)
    if not friend:
        raise InexistentUserException(f"ID#{friend_id}")
    return friend


def create_friend(creator, friend):
    """Create a new friend"""
    return Friend.objects.create(
        creator=creator,
        friend_user=friend,
    )
