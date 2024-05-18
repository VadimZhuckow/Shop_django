from django.urls import path
from weather.views import get_weather

urlpatterns = [
  path('weather/', get_weather),
]
