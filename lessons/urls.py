from django.urls import path

from .views import LessonViewSet

urlpatterns = [
    path(
        'lessons/',
        LessonViewSet.as_view({'post': 'create', 'get': 'list'}),
        name='lesson'
    )
]
