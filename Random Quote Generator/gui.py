import tkinter as tk
import requests

def get_quote():
    try:
        response = requests.get("https://zenquotes.io/api/random")
        data = response.json()
        return (f"{data[0]['q']} - {data[0]['a']}")
    except Exception as e:
        return "Could not fetch a quote. Please try again later."
    
def show_quote():
    quote = get_quote()
    quote_text.set(quote)

root = tk.Tk()
root.title("Random Quote Generator")
root.geometry("400x400")

quote_text = tk.StringVar()
quote_text.set("Click the button to get a quote!")

quote_label = tk.Label(root, textvariable=quote_text, justify="center", font=("Comic Sans MS",12),wraplength=350)
quote_label.pack(pady=40)

get_quote_button = tk.Button(root, text="Get Quote", command=show_quote, font=("Comic Sans MS",12))
get_quote_button.pack()


root.mainloop()
