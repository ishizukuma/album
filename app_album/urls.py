from django.urls import path

from . import views

app_name = 'app_album'
urlpatterns = [
    path('', views.IndexView.as_view(), name="login"),
    path('top/', views.TopView.as_view(), name="top"),
]
