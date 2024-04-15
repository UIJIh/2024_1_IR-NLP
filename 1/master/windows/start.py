import sys
sys.path.append('..')
from utils.buttons import *
from boolean import BooleanModelWindow
from vector import VectorModelWindow
import tkinter as tk
import csv

class StartWindow:
    def __init__(self, parent):
        self.parent = parent
        self.window = tk.Toplevel(parent)
        self.window.title("Select Model")
        self.window.geometry("600x350")
        self.window.iconbitmap("../images/main.ico")        
        self.model_message = (
            "\nHere you can experience two models.\n"
            "Please select an option below to proceed."
        )
        self.model_label = tk.Label(self.window, text=self.model_message, font=("Helvetica", 15))
        self.model_label.pack(padx=20, pady=30)
        self.boolean_model_button = tk.Button(self.window, text="1. Boolean Model", font=("Helvetica", 12), command=self.open_boolean_model)
        self.boolean_model_button.pack(pady=10)
        self.vector_model_button = tk.Button(self.window, text="2. Vector Model", font=("Helvetica", 12), command=self.open_vector_model)
        self.vector_model_button.pack(pady=10)
        self.back_button = BackButton(self.window, self.close_window)
        self.back_button.pack(pady=10)

        self.documents = []
        with open("../dataset/Korea_DB_0413.csv", mode='r', encoding='cp949') as file:
            reader = csv.DictReader(file)
            for row in reader:
                title = row['title']
                date=row['date']
                article = row['article']
                self.documents.append({'title': title, 'date':date, 'article': article})

    def close_window(self):
        self.window.destroy()

    def open_boolean_model(self):
        self.window.destroy()  
        boolean_model_window = BooleanModelWindow(self.parent, self.documents)

    def open_vector_model(self):
        self.window.destroy()  
        vector_model_window = VectorModelWindow(self.parent, self.documents)