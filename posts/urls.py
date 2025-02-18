from django.urls import include, path, re_path
from rest_framework.routers import DefaultRouter

from .views import (
    LatestPostsViaFollowAPIView,
    LatestPostsViaHandleAPIView,
    PostViewSet,
)

router = DefaultRouter()
router.register(r"p", PostViewSet)
router.register(r"follows", LatestPostsViaFollowAPIView, basename="follows")

urlpatterns = [
    path("", include(router.urls)),
    re_path(
        r"latest/(?P<handle>[a-z0-9._]+)/",
        LatestPostsViaHandleAPIView.as_view(),
        name="user-latest-posts",
    ),
]
