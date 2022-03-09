import requests as r
from django import forms
from django.core.exceptions import ValidationError

from servis.setting_environment import URL_WAY_POINTS



class CreateRouteForm(forms.Form):
    """Форма создания маршрута"""
    points = r.get(URL_WAY_POINTS).json()
    OPTIONS = []
    for point in points:
        OPTIONS.append((point['id'], f'{point["name"]} ({point["latitude"]}, {point["longitude"]})'))
    name = forms.CharField(max_length=15)
    startpoint = forms.ChoiceField(choices=OPTIONS)
    endpoint = forms.ChoiceField(choices=OPTIONS)

    def clean(self):
        cleaned_data = super(CreateRouteForm, self).clean()
        startpoint = cleaned_data.get('startpoint')
        endpoint = cleaned_data.get('endpoint')
        if startpoint == endpoint:
            raise ValidationError('Начальная и конечная точки не должны совпадать')
