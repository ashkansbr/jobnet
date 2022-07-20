from rest_framework.viewsets import ModelViewSet
from ..models import City, Province
from .serializers import ReadCitySerializer, WriteCitySerializer, ProvinceSerializer


class CityViewSet(ModelViewSet):
    queryset = City.objects.all()

    def get_serializer_class(self):
        if self.action in ['create', 'update']:
            return WriteCitySerializer
        return ReadCitySerializer


class ProvinceViewSet(ModelViewSet):
    queryset = Province.objects.all()
    serializer_class = ProvinceSerializer