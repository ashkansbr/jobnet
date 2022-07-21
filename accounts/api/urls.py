from rest_framework.routers import SimpleRouter
from .views import EmployerViewSet, JobSeekerViewSet

router = SimpleRouter()
router.register('employer', EmployerViewSet)
router.register('job-seeker', JobSeekerViewSet)

urlpatterns = router.urls
