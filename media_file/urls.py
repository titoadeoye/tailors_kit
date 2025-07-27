from rest_framework.routers import DefaultRouter
from media_file.views import MediaFileViewSet

router = DefaultRouter()
router.register(r'media', MediaFileViewSet, basename='mediafile')

urlpatterns = router.urls
