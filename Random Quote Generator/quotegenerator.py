import requests

response = requests.get("https://api.quotable.io/random")

data = response.json()
print(f"{data['content']} - {data['author']}")
