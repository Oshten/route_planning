from rest_framework import serializers

from waypoints import models


class WayPointSerializer(serializers.ModelSerializer):
    """Класс серилизатора точки маршрута"""
    class Meta:
        model = models.WayPoint
        fields = '__all__'


class CreateRouteSerializer(serializers.ModelSerializer):
    """Создание нового маршрута"""
    class Meta:
        model = models.Route
        fields = '__all__'

class RouteSerializer(serializers.ModelSerializer):
    """Вывод точек маршрута маршрута"""
    startpoint = WayPointSerializer(read_only=True)
    endpoint = WayPointSerializer(read_only=True)
    waypoints = WayPointSerializer(read_only=True, many=True)
    class Meta:
        model = models.Route
        fields = '__all__'
