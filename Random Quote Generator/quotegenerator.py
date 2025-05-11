import requests

response = requests.get("https://zenquotes.io/api/random")

data = response.json()
print(f"{data[0]['q']} - {data[0]['a']}")
