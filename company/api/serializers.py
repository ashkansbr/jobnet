from rest_framework import serializers
from ..models import Employee, Company, CompanyType, EmployeeType


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        exclude = ['company', 'updated_at']


class CompanySerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(read_only=True)
    employees = EmployeeSerializer(many=True, read_only=True)

    class Meta:
        model = Company
        exclude = ('employer', 'updated_at')


class EmployeeTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeType
        fields = ['type']


class CompanyTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyType
        fields = ['id', 'type']
        read_only_fields = ['id']
