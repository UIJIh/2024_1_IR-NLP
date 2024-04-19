import sys
sys.path.append('..')
from utils.buttons import *
import tkinter as tk

class BackButton:
    def __init__(self, parent, command):
        self.parent = parent
        self.command = command
        self.button = tk.Button(parent, text="Back", font=("Helvetica", 13), command=self.close_window)

    def pack(self, **kwargs):
        self.button.pack(**kwargs)

    def close_window(self):
        if self.command:
            self.command()
        else:
            self.parent.destroy()

class ExitButton:
    def __init__(self, parent, command):
        self.parent = parent
        self.command = command
        self.button = tk.Button(parent, text="Exit", font=("Helvetica", 13), command=self.close_window)

    def pack(self, **kwargs):
        self.button.pack(**kwargs)

    def close_window(self):
        if self.command:
            self.command()
        else:
            self.parent.destroy()