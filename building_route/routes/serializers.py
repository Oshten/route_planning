from rest_framework import serializers

from routes import models


class ListRoutesSerializer(serializers.ModelSerializer):
    """Сериализатор списка маршрутов"""
    class Meta:
        model = models.Route
        fields = '__all__'


class CreateRouteSerializer(serializers.ModelSerializer):
    """Создание нового маршрута"""
    class Meta:
        model = models.Route
        fields = '__all__'