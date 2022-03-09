import random

from waypoints import models
from waypoints import serializers

def make_route(startpoint, endpoint):
    """Прокладывание маршрута между начальной и конечной точкой"""

    #Логика построения маршрута (для ускорения точки выбираются случайным образом)
    all_points = models.WayPoint.objects.exclude(id=(startpoint)).exclude(id=endpoint)
    points_route_id = []
    quantity_points = random.randint(5, 10)
    while len(points_route_id) < quantity_points:
        point_id = random.choices(all_points)[0].id
        if not point_id in points_route_id:
            points_route_id.append(point_id)
    points = []
    for i in points_route_id:
        queryset = models.WayPoint.objects.get(id=i)
        serializer_for_queryset = serializers.WayPointSerializer(instance=queryset).data
        points.append(serializer_for_queryset)
    return points
