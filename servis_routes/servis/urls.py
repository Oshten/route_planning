from django.urls import path

from servis import views

urlpatterns = [
    path('waypoints/', views.WayPointsView.as_view(), name='list_waypoints'),
    path('route/', views.ListRoutesView.as_view(), name='list_routes'),
    path('route/<int:pk>', views.DetailsRouteView.as_view(), name='details_route'),
    path('route/create/', views.CreatRouteFormView.as_view(), name='create_new_route'),
]