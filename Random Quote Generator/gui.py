import tkinter as tk

root = tk.Tk()
root.title("Random Quote Generator")
root.geometry("400x400")

quote_text = tk.StringVar()
quote_text.set("Click the button to get a quote!")

quote_label = tk.Label(root, textvariable=quote_text, justify="center", font=("Comic Sans MS",12))
quote_label.pack(pady=40)


root.mainloop()
