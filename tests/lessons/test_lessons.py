import json
import pytest

from rest_framework import status
from rest_framework.test import (
    APIClient,
    APIRequestFactory,
)

from tests.factories.courses import CourseFactory
from tests.utils import new_user


@pytest.mark.django_db
def test_create_lesson(client, django_user_model):
    """
    Request should return 201
    """
    user, token = new_user(django_user_model)

    course = CourseFactory()

    # new lesson
    form_data = {
        "course_id": course.id
    }

    client = APIClient()
    client.force_authenticate(user=user)

    response = client.post(
        "/api/v1/lessons/",
        form_data,
        follow=True,
    )

    resp = response.json()

    assert response.status_code == status.HTTP_201_CREATED
    assert resp['user']['username'] == user.username
    assert resp['course']['name'] == course.name
