import tkinter as tk
import time
import threading
import random

class TypeSpeedGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Typing Speed Calculator')
        self.root.geometry("800x600")

        self.texts = open("C:\\mydataaaa\\workspace\\Python\\Codedex\\Codedex-repo\\Speed Typing Test\\texts.txt","r").read().split("\n")

        self.frame = tk.Frame(self.root)

        self.sample_label = tk.Label(self.frame, text=random.choice(self.texts),font=("Helvetica",12))
        self.sample_label.grid(row=0 , column=0 ,columnspan=2 , padx=5,pady=10)

        self.input_entry = tk.Entry(self.frame,width=40, font=("Helvetica",16))
        self.input_entry.grid(row=1, column=0, columnspan=2,padx=5,pady=10)
        self.input_entry.bind("<KeyRelease>",self.start)

        self.speed_label = tk.Label(self.frame, text="Speed: \n0.00 CPS\n0.00 CPM\n0.00 WPS\n0.00 WPM",font=("Helvetica",12))
        self.speed_label.grid(row=2 , column=0 ,columnspan=2 , padx=5,pady=10)     

        self.reset_button = tk.Button(self.frame, text="Reset", command=self.reset, font=("Helvetica",12))
        self.reset_button.grid(row=3 , column=0 ,columnspan=2 , padx=5,pady=10) 

        self.frame.pack(expand=True)

        self.counter = 0
        self.running = False

        self.root.mainloop()

    def start(self, event):
        if not self.running:
            if not event.keycode in [16,1,18]:
                self.running = True
                t = threading.Thread(target=self.time_thread)
                t.start()
        if not self.sample_label.cget('text').startswith(self.input_entry.get()):
            self.input_entry.config(fg = "red")
        else:
            self.input_entry.config(fg="black")
        if self.input_entry.get() == self.sample_label.cget('text'):
            self.running = False
            self.input_entry.config(fg="green")

    def time_thread(self):
        while self.running:
            time.sleep(0.1)
            self.counter += 0.1
            cps = len(self.input_entry.get()) / self.counter
            cpm = cps * 60
            wps = len(self.input_entry.get().split(" ")) / self.counter
            wpm = wps * 60
            self.speed_label.config(text=f"Speed: \n{cps:.2f} CPS\n{cpm:.2f} CPM\n {wps:.2f}WPS\n{wpm:.2f} WPM")

    def reset(self):
        self.running = False
        self.counter = 0
        self.speed_label.config(text="Speed: \n0.00 CPS\n0.00 CPM\n0.00 WPS\n0.00 WPM")
        self.sample_label.config(text=random.choice(self.texts))
        self.input_entry.delete(0, tk.END)

TypeSpeedGUI()

