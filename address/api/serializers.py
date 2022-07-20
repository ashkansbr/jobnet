from rest_framework import serializers
from ..models import Province, City


class ProvinceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Province
        fields = ['name', 'slug']


class ReadCitySerializer(serializers.ModelSerializer):
    province = ProvinceSerializer()

    class Meta:
        model = City
        fields = ['name', 'slug', 'province']


class WriteCitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['name', 'slug', 'province']