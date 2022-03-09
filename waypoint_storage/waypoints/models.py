from django.db import models


class WayPoint(models.Model):
    """Модель точки маршрута"""
    name = models.CharField(max_length=30, verbose_name='название')
    latitude = models.CharField(max_length=6, verbose_name='широта')
    longitude = models.CharField(max_length=6, verbose_name='долгота')

    def __str__(self):
        """Отображение модели точки маршрута"""
        return f'{self.name} ({self.latitude}, {self.longitude})'
    
    
class Route(models.Model):
    """Модель точек маршрута"""
    name = models.CharField(max_length=30)
    author = models.CharField(max_length=30)
    startpoint = models.ForeignKey(WayPoint, on_delete=models.CASCADE, related_name='startpoint', null=True)
    endpoint = models.ForeignKey(WayPoint, on_delete=models.CASCADE, related_name='endpoint', null=True)
    waypoints = models.ManyToManyField(WayPoint, null=True)
    


