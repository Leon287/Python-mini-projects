import datetime as dt
import requests
from dotenv import load_dotenv
import os
# use .env file to store your API key
# Load environment variables
load_dotenv()

BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
#Load the API KEY securely from env file (from the environment)
API_KEY = os.getenv('api_key')
CITY = input("Enter City: ")

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

print(f"Temperature in {CITY}: {temp_celsius:.2f}°C or {temp_farenheit:.2f}°F")
print(f"Temperature in {CITY} feels like: {feels_like_celsius:.2f}°C or {feels_like_fahrenheit:.2f}°F")
print(f"Humidity in {CITY}: {huimidity}%")
print(f"Wind speed in {CITY}: {wind_speed}m/s")
print(f"General Weather in {CITY}: {description}")
print(f"Sunrise in {CITY} at {sunrise_time}")
print(f"Sunset in {CITY} at {sunset_time}")