import tkinter as tk
import time
import threading
import random

class TypeSpeddGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Typing Speed Calculator')
        self.root.geometry("800x600")

        self.texts = open("texts.txt","r").read().split("\n")

        self.frame = tk.Frame(self.root)

        self.sample_label = tk.label(self.frame, text=random.choice(self.texts),font=("Helvetica",18))
        self.sample_label.grid(row=0 , column=0 ,columnspan=2 , padx=5,pady=10)

        self.input_entry = tk.Entry(self.frame,width=40, font=("Helvetica",24))
        self.input_entry.grid(row=1, column=0, columnspan=2,padx=5,pady=10)
        self.input_entry.bind("<KeyDown>",self.start)

        self.speed_label = tk.label(self.frame, text="Speed: \n0.00 CPS\n0.00 CPM",font=("Helvetica",18))
        self.speed_label.grid(row=2 , column=0 ,columnspan=2 , padx=5,pady=10)     

        self.reset_button = tk.Button(self.frame, text="Reset", command=self.reset)
        self.reset_button.grid(row=3 , column=0 ,columnspan=2 , padx=5,pady=10) 

        self.frame.pack(expand=True)

        self.counter = 0
        self.started = False

        self.root.mainloop()

    def start(self):
        pass

    def time_thread(self):
        pass

    def reset(self):
        pass