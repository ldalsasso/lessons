from django.contrib.auth.models import User


def get_user(user_id):
    """ get user by id"""
    user = None
    try:
        return User.objects.get(id=user_id)
    except Exception:
        return user
