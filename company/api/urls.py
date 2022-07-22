from rest_framework.routers import SimpleRouter
from company.api.views import CompanyViewSet, CompanyTypeViewSet, EmployeeViewSet, EmployeeTypeViewSet

app_name = 'company'

router = SimpleRouter()

router.register('employee', EmployeeViewSet)
router.register('employee-type', EmployeeTypeViewSet)
router.register('', CompanyViewSet)
router.register('company-type', CompanyTypeViewSet)


urlpatterns = router.urls
