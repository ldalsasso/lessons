from datetime import datetime
from pytz import timezone as pytz_timezone

from django.conf import settings


def get_current_time(timezone_str=None):
    """
    Get and return the current time of a given place.

    :param timezone_str: The timezone string for the location, defaulted to
        the one of Buenos Aires, Argentina.
    :return: The datetime object with the current time for the given place.
    """
    if timezone_str is None:
        timezone_str = settings.TIME_ZONE

    tz_obj = pytz_timezone(timezone_str)
    now_time = datetime.now(tz_obj)
    return now_time
