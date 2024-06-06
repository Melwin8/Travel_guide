from django.urls import path
from .views import *

urlpatterns = [
    path('weather/<str:cityname>/', WeatherAPIView.as_view()),

]