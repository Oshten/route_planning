from random import randint
from django.core.management.base import BaseCommand

from waypoints import models

def generation_coordinates():
    coordinate = ''
    for _ in range(6):
        coordinate += str(randint(0, 9))
    return coordinate

class Command(BaseCommand):
    """Пользовательская команда
    Генерация случайный точек маршрута"""
    help = 'Waypoint generation'

    def handle(self, *args, **kwargs):
        for namber in range(50):
            way_point = models.WayPoint(
                name=f'waypoint_{namber + 1}',
                latitude=generation_coordinates(),
                longitude=generation_coordinates()
            )
            way_point.save()
