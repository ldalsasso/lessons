from django.urls import include, path
from rest_framework import routers

from .views import UserViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('user/auth/', include('timed_auth_token.urls')),
]
