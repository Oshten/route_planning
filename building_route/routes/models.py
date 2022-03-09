from django.db import models


class Route(models.Model):
    """Модель точек маршрута"""
    name = models.CharField(max_length=15, verbose_name='Название маршрута')
    startpoint = models.TextField(verbose_name='Начальная точка маршрута', null=True)
    endpoint = models.TextField(verbose_name='Конечная точка маршрута', null=True)
    waypoints = models.TextField(verbose_name='Точки маршрутов', null=True)
    author = models.TextField(verbose_name='Автор маршрута')

