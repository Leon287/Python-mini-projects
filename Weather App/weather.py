import datetime as dt
import requests
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
API_KEY = os.getenv('api_key')
CITY = "London"

# Build URL with correct formatting
url = f"{BASE_URL}appid={API_KEY}&q={CITY}"

# Make the request and print the response
response = requests.get(url)
data = response.json()

print(data)

