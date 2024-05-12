from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render

from weather_api import current_weather


# Create your views here.


def get_weather(request: HttpRequest) -> HttpResponse:
    if request.method == "GET":
        return JsonResponse(
            current_weather(59.93, 30.31),
            json_dumps_params={
                "indent": 4,
                "ensure_ascii": False
            }
        )

