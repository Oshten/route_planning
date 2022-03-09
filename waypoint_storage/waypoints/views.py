import json
import random
from django.db.models import Q
from rest_framework.response import Response
from rest_framework import views

from waypoints import serializers
from waypoints import models
from waypoints import functions

class WayPointsView(views.APIView):
    """Класс представления путевых точек в формате JSON"""
    def get(self, request):
        queryset = models.WayPoint.objects.all()
        serializer_for_queryset = serializers.WayPointSerializer(instance=queryset, many=True)
        return Response(serializer_for_queryset.data)


class WayPointDetailView(views.APIView):
    """Класс представления точки в формате JSON"""
    def get(self, request, pk):
        queryset = models.WayPoint.objects.get(id=pk)
        serializer_for_queryset = serializers.WayPointSerializer(instance=queryset)
        return Response(serializer_for_queryset.data)

class WayPointsRouteView(views.APIView):
    """Класс представления точек маршрута в формате JSON"""
    def get(self, request, startpoint_endpoint):
        startpoint_id = startpoint_endpoint[:(startpoint_endpoint.index('-'))]
        endpoint_id = startpoint_endpoint[(startpoint_endpoint.index('-'))+1:]
        queryset_data = functions.make_route(startpoint_id, endpoint_id)
        return Response(queryset_data)








