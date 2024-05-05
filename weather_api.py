import requests
import json
from datetime import datetime
access_key = '66ee5a8b-a5f1-4115-8e0b-6bf7e08c1c8b'


def current_weather(lat, lon):

    url = f"https://api.weather.yandex.ru/v2/forecast?lat={lat}&lon={lon}"
    headers = {
        'X-Yandex-Weather-Key': access_key
    }

    response = requests.get(url, headers=headers).json()
    res_ = json.dumps(response, indent=4)

    result = {
            'Город': response["geo_object"]["locality"]["name"],
            'Время': datetime.fromtimestamp(response["now"]).strftime("%H:%M"),
            'Температура': response["fact"]["temp"],
            'Ощущается как': response['fact']['feels_like'],  # TODO Реализовать вычисление ощущаемой температуры из данных полученных от API
            'Давление': response['fact']['pressure_mm'],  # TODO Реализовать вычисление давления из данных полученных от API
            'Влажность': response['fact']['humidity'],  # TODO Реализовать вычисление влажности из данных полученных от API
            # 'wind_speed': 'реализация',  # TODO Реализовать вычисление скорости ветра из данных полученных от API
            'Скорость ветра': response['fact']['wind_speed'],  # TODO Реализовать вычисление скорости порывов ветка из данных полученных от API
            'Направление ветра': response['fact']['wind_dir'],  # Если используете Тариф «Погода на вашем сайте», то закомментируйте эту строку
        }
    # print(response["geo_object"]["locality"]["name"])
    # print(res_)
    return result
    # for key, value in result.items():
    #
    #     print(f'{key} : {value}')








if __name__ == "__main__":
    print(current_weather(59.93, 30.31))
