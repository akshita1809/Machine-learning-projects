#asks a user to input a city or town and retuens to the user details of weather in that location
#using https://openweathermap.org/api

import requests
from pprint import pprint

API_key = 'adbe5dd0c51324fdf2c4d08497b298d5'

city = input ('Enter a city:')
base_url = 'http://api.openweathermap.org/data/2.5/weather?appid=' + API_key + '&q=' + city

weather_data = requests.get(base_url).json()

pprint(weather_data)