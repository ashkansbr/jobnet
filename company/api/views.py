from rest_framework.viewsets import ModelViewSet
from company.api.serializers import EmployeeSerializer, CompanySerializer,\
    CompanyTypeSerializer, EmployeeTypeSerializer
from company.models import Employee, EmployeeType, Company, CompanyType


class CompanyViewSet(ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class CompanyTypeViewSet(ModelViewSet):
    queryset = CompanyType.objects.all()
    serializer_class = CompanyTypeSerializer


class EmployeeViewSet(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeTypeViewSet(ModelViewSet):
    queryset = EmployeeType.objects.all()
    serializer_class = EmployeeTypeSerializer