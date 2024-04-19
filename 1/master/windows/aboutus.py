import sys
sys.path.append('..')
from utils.buttons import *
import tkinter as tk

class AboutUsWindow:
    def __init__(self, parent):
        self.parent = parent
        self.window = tk.Toplevel(parent)
        self.window.title("About Us")
        self.window.geometry("600x350")
        self.window.iconbitmap("../images/about.ico")
        self.about_us_message = (
        "\nOur Information Retrieval System is designed to easily detect social events.\n\n"
        "In particular, we have focused on the \'South Korean Election\', \na significant social event in South Korea.\n\n"
        "We collected data from January 10th to April 10th \nto analyze the importance and impact of the election.\n\n"
        "Our system allows users to search for specific keywords \nrelated to the election \nand see how many articles "
        "contain those keywords during the specified period.\n\n"
        "Through this, users can detect how important the event was \nand how much it was discussed during that period."
        )
        self.about_us_label = tk.Label(self.window, text=self.about_us_message, font=("Helvetica", 12))
        self.about_us_label.pack(padx=20, pady=10)

        self.back_button = ExitButton(self.window, self.close_window)
        self.back_button.pack(pady=10)

    def close_window(self):
        self.window.destroy()