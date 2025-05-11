import requests

def get_quote():
    try:
        response = requests.get("https://zenquotes.io/api/random")
        data = response.json()
        return (f"{data[0]['q']} - {data[0]['a']}")
    except Exception as e:
        return "Could not fetch a quote. Please try again later."

while True:
    quote = get_quote()
    print(f"\n{quote}\n")
    again = input("Do you want another quote? (y/n) :").strip().lower()
    if again != 'y':
        print("Goodbye")
        break
