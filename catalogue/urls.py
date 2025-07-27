from rest_framework.routers import DefaultRouter
from catalogue.views import CatalogueItemViewSet

router = DefaultRouter()
router.register(r"catalogue", CatalogueItemViewSet, basename="catalogue")

urlpatterns = router.urls
