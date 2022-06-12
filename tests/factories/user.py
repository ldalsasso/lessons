from django.template.defaultfilters import slugify

import factory

from factory import (
    lazy_attribute,
    SelfAttribute,
    SubFactory,
)
from factory.django import DjangoModelFactory
import faker

from common.utils import get_current_time

faker = faker.Factory.create()


class UserFactory(DjangoModelFactory):

    class Meta:
        model = 'auth.User'
        django_get_or_create = ('username',)

    first_name = lazy_attribute(lambda o: faker.first_name())
    last_name = lazy_attribute(lambda o: faker.last_name())
    username = lazy_attribute(
        lambda o: slugify(o.first_name + '.' + o.last_name))
    email = lazy_attribute(lambda o: faker.email())
    is_superuser = True
