import faker
from faker.providers import string

from timed_auth_token.models import TimedAuthToken


faker = faker.Factory.create()
faker.add_provider(string)


def new_user(django_user_model, username='jhunt', password='jhunt'):
    user = django_user_model.objects.create_user(username=username, password=password)
    token = TimedAuthToken.objects.create(user=user)
    return user, token
