from rest_framework.routers import SimpleRouter
from .views import ResumeViewSet

router = SimpleRouter()

router.register('resume', ResumeViewSet)

urlpatterns = router.urls
