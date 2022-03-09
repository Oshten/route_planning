from django.urls import path

from routes import views


urlpatterns = [
    path('route/', views.ListRoutesView.as_view()),
    path('route/<int:pk>', views.DetailsRouterView.as_view()),
    path('create', views.CreateRouteView.as_view()),
]