import requests

def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    data = response.json()
    return (f"{data[0]['q']} - {data[0]['a']}")

while True:
    quote = get_quote()
    print(f"\n{quote}\n")
    again = input("Do you want another quote? (y/n) :")
    if again != 'y':
        print("Goodbye")
        break
