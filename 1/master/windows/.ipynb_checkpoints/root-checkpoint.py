import sys
sys.path.append('..')
from windows.start import StartWindow
from windows.aboutus import AboutUsWindow
from utils.effect import *
import tkinter as tk

def main():
    root = tk.Tk()
    root.title("Welcome to our IR System")
    root.geometry("600x350")  
    root.iconbitmap("../images/main.ico")  

    welcome_message_1 = (
        "\nWelcome to Our IR System!"
    )
    welcome_message_2 = (
        "This system allows you to search for information easily.\n"
        "It also enables you to detect social events.\n"
        "Please select an option below to get started."
    )
    welcome_label_1 = tk.Label(root, text=welcome_message_1, font=("Helvetica", 20))
    welcome_label_1.pack(pady=10)
    welcome_label_2 = tk.Label(root, text=welcome_message_2, font=("Helvetica", 15))
    welcome_label_2.pack(pady=20)

    # "Start" button
    def open_start_window():
        StartWindow(root)

    start_button = tk.Button(root, text="Start!", font=("Helvetica", 13), command=open_start_window)
    start_button.pack(pady=10)
    flash_text(start_button)

    # "About us" button
    def open_about_us_window():
        AboutUsWindow(root)

    about_us_button = tk.Button(root, text="About Us", font=("Helvetica", 12), command=open_about_us_window)
    about_us_button.pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    main()
