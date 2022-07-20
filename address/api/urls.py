from rest_framework.routers import SimpleRouter
from .views import ProvinceViewSet, CityViewSet


router = SimpleRouter()

router.register('city', CityViewSet)
router.register('province', ProvinceViewSet)

urlpatterns = router.urls
