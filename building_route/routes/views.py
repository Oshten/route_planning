import requests as r
from rest_framework.response import Response
from rest_framework import views
from rest_framework import generics

from routes import serializers
from routes import models
from routes.setting_environment import URL_WAY_POINTS


class ListRoutesView(views.APIView):
    """Представление списка маршрутов"""
    def get(self, request):
        queryset = models.Route.objects.all()
        serializer_for_queryset = serializers.ListRoutesSerializer(instance=queryset, many=True)
        return Response(serializer_for_queryset.data)


class DetailsRouterView(views.APIView):
    """Представление детальной информации о маршруте"""
    def get(self, request, pk):
        queryset = models.Route.objects.get(id=pk)
        serializer_for_queryset = serializers.ListRoutesSerializer(instance=queryset)
        return Response(serializer_for_queryset.data)



class CreateRouteView(views.APIView):
    """Создание нового маршрута"""
    def post(self, request):
        startpoint_id = request.data.get('startpoint')
        startpoint = r.get(URL_WAY_POINTS+startpoint_id).json()
        endpoint_id = request.data.get('endpoint')
        endpoint = r.get(URL_WAY_POINTS+endpoint_id).json()
        startpoint_endpoint = f'{startpoint_id}-{endpoint_id}'
        waypoints = r.get(URL_WAY_POINTS+startpoint_endpoint).json()
        data = {
            'name': request.data.get('name'),
            'author': request.data.get('author'),
            'startpoint': startpoint,
            'endpoint': endpoint,
            'waypoints': waypoints,
        }
        queruset = models.Route(**data)
        queruset.save()
        serializer_for_queryset = serializers.CreateRouteSerializer(queruset)
        return Response(serializer_for_queryset.data, status=201)


