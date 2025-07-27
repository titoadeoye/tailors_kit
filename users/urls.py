from rest_framework.routers import DefaultRouter
from users.views import UserViewSet, user_metrics
from django.urls import path


router = DefaultRouter()
router.register(r"users", UserViewSet, basename="user")

urlpatterns = [
    *router.urls,
    path("dashboard/", user_metrics, name="dashboard"),
]
