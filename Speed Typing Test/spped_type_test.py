import tkinter as tk
import time
import threading
import random

class TypeSpeddGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Typing Speed Calculator')
        self.root.geometry("800x600")

        self.sample_label = tk.label(self.root, text="")