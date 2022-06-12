from django.urls import path

from .views import FriendViewSet

urlpatterns = [
    path(
        'friends/',
        FriendViewSet.as_view({'post': 'create', 'get': 'list'}),
        name='friend'
    )
]
