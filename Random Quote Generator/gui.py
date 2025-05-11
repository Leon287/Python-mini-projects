import tkinter as tk
import requests

def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    response.raise_for_status()
    data = response.json()
    quote = f'"{data[0]["q"]}" - {data[0]["a"]}'
    quote_text.set(quote)

root = tk.Tk()
root.title("Random Quote Generator")
root.geometry("400x400")

quote_text = tk.StringVar()
quote_text.set("Click the button to get a quote!")

quote_label = tk.Label(root, textvariable=quote_text, justify="center", font=("Comic Sans MS",12))
quote_label.pack(pady=40)

get_quote_button = tk.Button(root, text="Get Quote", command=get_quote(), font=("Comic Sans MS",12))
get_quote_button.pack()


root.mainloop()
