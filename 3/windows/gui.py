# # gui.py
# import tkinter as tk
# from tkinter import messagebox
# from tkinter.scrolledtext import ScrolledText
# import random
# from models.vsm import VSMModel

# class MovieFinder(tk.Tk):
#     def __init__(self, vsm_model, trans_model):
#         super().__init__()
#         self.title("Movie Finder")
#         self.geometry("500x350")
#         self.show_main_menu()
#         self.flash_text()
#         # 모델 초기화
#         self.vsm_model = vsm_model
#         self.trans_model = trans_model  

#     def flash_text(self):
#         if hasattr(self, 'title_label') and self.title_label.winfo_exists():
#             color = random.choice(['blue', 'darkblue'])
#             self.title_label.config(fg=color)
#             self.after(300, self.flash_text)

#     def show_main_menu(self):
#         for widget in self.winfo_children():
#             widget.destroy()
#         self.title_label = tk.Label(self, text="🎬 Movie Finder 🎬", font=("Comic Sans MS", 17, 'bold'), bg='lightblue', fg='blue')
#         self.title_label.pack(pady=50)
#         self.find_movie_button = tk.Button(self, text="Search Movie", width=15, command=self.show_options_menu, bg='lightblue', fg='darkblue', font=("Comic Sans MS", 12))
#         self.find_movie_button.pack(pady=12)
#         self.exit_button = tk.Button(self, text="Exit", width=15, command=self.destroy, bg='lightblue', fg='darkblue', font=("Comic Sans MS", 12))
#         self.exit_button.pack(pady=12)

#     def show_options_menu(self):
#         for widget in self.winfo_children():
#             widget.destroy()
#         self.title_label = tk.Label(self, text="🍿 Select Movie Search Method 🍿", font=("Comic Sans MS", 17, 'bold'), bg='lightblue', fg='blue')
#         self.title_label.pack(pady=30)
#         self.vsm_button = tk.Button(self, text="1.VSM", width=15, command=self.find_movie_vsm, bg='lightblue', fg='darkblue', font=("Comic Sans MS", 12))
#         self.vsm_button.pack(pady=12)
#         self.TRANSFORMER_button = tk.Button(self, text="2.TRANSFORMER", width=15, command=self.find_movie_TRANSFORMER, bg='lightblue', fg='darkblue', font=("Comic Sans MS", 12))
#         self.TRANSFORMER_button.pack(pady=12)
#         self.back_button = tk.Button(self, text="Back", width=15, command=self.show_main_menu, bg='lightblue', fg='darkblue', font=("Comic Sans MS", 12))
#         self.back_button.pack(pady=12)

#     def find_movie_vsm(self):
#         self.find_movie(method="VSM")

#     def find_movie_TRANSFORMER(self):
#         self.find_movie(method="TRANSFORMER")

#     def find_movie(self, method):
#         for widget in self.winfo_children():
#             widget.destroy()
#         self.title_label = tk.Label(self, text=f"Enter a Query ({method}):", bg='lightblue', font=("Comic Sans MS", 13))
#         self.title_label.pack(pady=7)
#         self.movie_query = tk.Entry(self, font=("Comic Sans MS", 12))
#         self.movie_query.pack(pady=5)
#         self.search_button = tk.Button(self, text="Search", command=lambda: self.display_movie_info(method), bg='lightblue', font=("Comic Sans MS", 10))
#         self.search_button.pack(pady=7)
#         self.back_button = tk.Button(self, text="Back", command=self.show_options_menu, bg='lightblue', font=("Comic Sans MS", 10))
#         self.back_button.pack(pady=5)

#     def display_movie_info(self, method):
#         movie_query = self.movie_query.get().strip()
#         if not movie_query:
#             messagebox.showerror("Error", "Movie query cannot be empty!")
#             return

#         if method == "VSM":
#             similar_movies = self.vsm_model.find_similar_movies(movie_query)
#         elif method == "TRANSFORMER":
#             similar_movies = self.trans_model.find_similar_movies(movie_query)
#         else:
#             messagebox.showerror("Error", "Invalid search method.")
#             return

#         if similar_movies:
#             movie_info = "\n".join([f"{title} (Score: {score:.2f})" for title, score in similar_movies])
#         else:
#             movie_info = "No results found for the given query."

#         self.show_movie_info_window(movie_query, movie_info)

#     def show_movie_info_window(self, title, info):
#         info_window = tk.Toplevel(self)
#         info_window.title(title)
#         info_window.geometry("400x300")
#         info_window.configure(bg='lightblue')
        
#         title_label = tk.Label(info_window, text=title, font=("Comic Sans MS", 15, 'bold'), bg='lightblue')
#         title_label.pack(pady=10)
        
#         info_text = ScrolledText(info_window, width=50, height=10, wrap=tk.WORD, font=("Comic Sans MS", 12))
#         info_text.pack(pady=10)
#         info_text.insert(tk.END, info)
#         info_text.configure(state='disabled')

#         close_button = tk.Button(info_window, text="Close", command=info_window.destroy, bg='lightblue', font=("Comic Sans MS", 10))
#         close_button.pack(pady=10)

# gui.py
import tkinter as tk
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText
import random

class MovieFinder(tk.Tk):
    def __init__(self, vsm_model, trans_model):
        super().__init__()
        self.title("Movie Finder")
        self.geometry("500x350")
        self.configure(bg="#f0f0f0")  # Set background color
        self.show_main_menu()
        self.flash_text()
        # 모델 초기화
        self.vsm_model = vsm_model
        self.trans_model = trans_model  

    def flash_text(self):
        if hasattr(self, 'title_label') and self.title_label.winfo_exists():
            color = random.choice(['#007bff', '#004085'])  # Blue shades
            self.title_label.config(fg=color)
            self.after(300, self.flash_text)

    def show_main_menu(self):
        for widget in self.winfo_children():
            widget.destroy()
        self.title_label = tk.Label(self, text="🎬 Movie Finder 🎬", font=("Arial", 24, 'bold'), bg="#f0f0f0", fg="#007bff")  # Blue color
        self.title_label.pack(pady=50)
        self.find_movie_button = tk.Button(self, text="Search Movie", width=15, command=self.show_options_menu, bg="#007bff", fg="white", font=("Arial", 12, 'bold'))  # Blue button
        self.find_movie_button.pack(pady=12)
        self.exit_button = tk.Button(self, text="Exit", width=15, command=self.destroy, bg="#dc3545", fg="white", font=("Arial", 12, 'bold'))  # Red button
        self.exit_button.pack(pady=12)

    def show_options_menu(self):
        for widget in self.winfo_children():
            widget.destroy()
        self.title_label = tk.Label(self, text="🍿 Select Movie Search Method 🍿", font=("Arial", 20, 'bold'), bg="#f0f0f0", fg="#007bff")
        self.title_label.pack(pady=35)
        self.vsm_button = tk.Button(self, text="1. VSM", width=15, command=self.find_movie_vsm, bg="#007bff", fg="white", font=("Arial", 12, 'bold'))
        self.vsm_button.pack(pady=12)
        self.TRANSFORMER_button = tk.Button(self, text="2. TRANSFORMER", width=15, command=self.find_movie_TRANSFORMER, bg="#007bff", fg="white", font=("Arial", 12, 'bold'))
        self.TRANSFORMER_button.pack(pady=12)
        self.back_button = tk.Button(self, text="Back", width=15, command=self.show_main_menu, bg="#dc3545", fg="white", font=("Arial", 12, 'bold'))
        self.back_button.pack(pady=12)

    def find_movie_vsm(self):
        self.find_movie(method="VSM")

    def find_movie_TRANSFORMER(self):
        self.find_movie(method="TRANSFORMER")

    def find_movie(self, method):
        for widget in self.winfo_children():
            widget.destroy()
        self.title_label = tk.Label(self, text=f"Enter a Query ({method}):", bg="#f0f0f0", font=("Arial", 18))
        self.title_label.pack(pady=7)
        self.movie_query = tk.Entry(self, font=("Arial", 14))
        self.movie_query.pack(pady=5)
        self.search_button = tk.Button(self, text="Search", command=lambda: self.display_movie_info(method), bg="#007bff", fg="white", font=("Arial", 12, 'bold'))
        self.search_button.pack(pady=7)
        self.back_button = tk.Button(self, text="Back", command=self.show_options_menu, bg="#dc3545", fg="white", font=("Arial", 12, 'bold'))
        self.back_button.pack(pady=5)

    def display_movie_info(self, method):
        movie_query = self.movie_query.get().strip()
        if not movie_query:
            messagebox.showerror("Error", "Movie query cannot be empty!")
            return

        if method == "VSM":
            similar_movies = self.vsm_model.find_similar_movies(movie_query)
        elif method == "TRANSFORMER":
            similar_movies = self.trans_model.find_similar_movies(movie_query)
        else:
            messagebox.showerror("Error", "Invalid search method.")
            return

        if similar_movies:
            movie_info = "\n".join([f"{title}" for title in similar_movies])
        else:
            movie_info = "No results found for the given query."

        self.show_movie_info_window(movie_query, movie_info)

    def show_movie_info_window(self, title, info):
        info_window = tk.Toplevel(self)
        info_window.title(title)
        info_window.geometry("400x300")
        info_window.configure(bg="#f0f0f0")
        
        title_label = tk.Label(info_window, text=title, font=("Arial", 18, 'bold'), bg="#f0f0f0")
        title_label.pack(pady=10)
        
        info_text = ScrolledText(info_window, width=50, height=10, wrap=tk.WORD, font=("Arial", 12))
        info_text.pack(pady=10)
        info_text.insert(tk.END, info)
        info_text.configure(state='disabled')

        close_button = tk.Button(info_window, text="Close", command=info_window.destroy, bg="#dc3545", fg="white", font=("Arial", 12, 'bold'))
        close_button.pack(pady=10)
