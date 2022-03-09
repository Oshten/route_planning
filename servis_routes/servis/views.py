import requests as r
import json
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django import views

from servis import forms
from servis import setting_environment as s_v
from servis import functions



class WayPointsView(views.View):
    """ Пердставления всех навигационных точек """
    def get(self, request):
        try:
            way_points = r.get(s_v.URL_WAY_POINTS).json()
            message = None
        except r.exceptions.ConnectionError:
            message = 'Список точек временно не доступен. Попробуйте попозже.'
            way_points = None
        return render(request, 'servis/waypoints.html', context={'way_points': way_points, 'message': message})


class CreatRouteFormView(views.View):
    """Представление формы для создания нового маршрута"""
    def get(self, request):
        new_route = forms.CreateRouteForm()
        return render(request, 'servis/create_route.html', context={'new_route': new_route})

    def post(self, request):
        new_route = forms.CreateRouteForm(request.POST)
        if new_route.is_valid():
            data = new_route.cleaned_data
            data['author'] = request.user.get_username()
            r.post(s_v.URL_CREATE_ROUTE, data=new_route.cleaned_data)
            return redirect(to='/route/')
        return render(request, 'servis/create_route.html', context={'new_route': new_route})




class ListRoutesView(views.View):
    """Представление списка маршрутов"""
    def get(self, request):
        try:
            routes = r.get(s_v.URL_LIST_ROUTE).json()
            for route in routes:
                route['startpoint'] = json.loads(route['startpoint'].replace("'", '"'))
                route['endpoint'] = json.loads(route['endpoint'].replace("'", '"'))
            message = None
        except r.exceptions.ConnectionError:
            routes = None
            message = 'Список маршрутов временно не доступен. Попробуйте попозже.'
        return render(request, 'servis/list_routes.html', context={'routes': routes, 'message': message})


class DetailsRouteView(views.View):
    """Детальное представление маршрута"""
    def get(self, request, pk):
        try:
            route = r.get(s_v.URL_LIST_ROUTE + str(pk)).json()
            route = functions.determining_length_route(route)
            message = None
        except r.exceptions.ConnectionError:
            route = None
            message = 'Маршрут временно недоступет. Попробуйте позже.'
        return render(request, 'servis/details_routes.html', context={'route': route, 'message': message})





