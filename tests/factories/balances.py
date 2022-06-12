from django.template.defaultfilters import slugify

import factory

from factory import (
    LazyFunction,
    lazy_attribute,
    SelfAttribute,
    SubFactory,
)
from factory.django import DjangoModelFactory
import faker

from common.constants import TICKER_CHOICES
from common.utils import get_current_time

from balances.models import Balance

from .utils import get_random_choice_from_choices

faker = faker.Factory.create()


class BalanceFactory(DjangoModelFactory):

    class Meta:
        model = Balance

    amount = 500
    ticker = LazyFunction(
        lambda: get_random_choice_from_choices(
            TICKER_CHOICES
        )
    )
    updated = get_current_time()
