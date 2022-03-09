from django.urls import path

from waypoints import views


urlpatterns = [
    path('', views.WayPointsView.as_view()),
    path('<int:pk>', views.WayPointDetailView.as_view()),
    path('<slug:startpoint_endpoint>', views.WayPointsRouteView.as_view()),
]