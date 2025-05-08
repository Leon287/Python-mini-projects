import datetime as dt
import requests
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
API_KEY = os.getenv('api_key')
CITY = "London"

def kelvin_to_celsiuse_fahrenheit(kelvin):
    celsius = kelvin - 273.15
    farhenheit = celsius * (9/5) + 32
    return celsius, farhenheit

url = f"{BASE_URL}appid={API_KEY}&q={CITY}"
response = requests.get(url).json()

temp_kelvin = response['main']['temp']
temp_celsius , temp_farenheit = kelvin_to_celsiuse_fahrenheit(temp_kelvin)

feels_like_kelvin = response['main']['feels_like']
feels_like_celsius, feels_like_fahrenheit = kelvin_to_celsiuse_fahrenheit(feels_like_kelvin)

huimidity = response['main']['humidity']
description = response['weather'][0]['description']
sunrise_time = dt.datetime.utcfromtimestamp(response['sys']['sunrise'] + response['timezone'])
sunset_time = dt.datetime.utcfromtimestamp(response['sys']['sunset'] + response['timezone'])
wind_speed = response['wind']['speed']

