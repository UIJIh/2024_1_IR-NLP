import sys
sys.path.append('..')
from models.vectorModel import *
from utils.buttons import *
from utils.effect import *
from utils.graph import *
import tkinter as tk
from tkinter import scrolledtext, messagebox
import matplotlib.pyplot as plt

class VectorModelWindow:
    def __init__(self, parent, documents):
        self.parent = parent
        self.documents = documents
        self.results = None
        
        self.window = tk.Toplevel(parent)
        self.window.title("Vector Model")
        self.window.geometry("800x600")
        self.window.iconbitmap("../images/main.ico")
        
        self.query_label = tk.Label(self.window, text="Enter your query:", font=("Helvetica", 12))
        self.query_label.pack(pady=5)
        
        query_frame = tk.Frame(self.window)
        query_frame.pack(pady=5)

        self.query_entry = tk.Entry(query_frame, width=65)
        self.query_entry.pack(side=tk.LEFT, padx=5)
        
        self.search_button = tk.Button(query_frame, text="Search", font=("Helvetica", 12), command=self.search)
        self.search_button.pack(side=tk.LEFT)

        button_frame = tk.Frame(self.window)
        button_frame.pack(pady=5)      
        
        self.show_graph_button = tk.Button(button_frame, text="Social Event Visualization", font=("Helvetica", 12), command=self.show_graph)
        self.show_graph_button.pack(side=tk.RIGHT, padx=5)
        flash_text(self.show_graph_button)
        
        self.back_button = ExitButton(button_frame, self.close_window)
        self.back_button.pack(side=tk.LEFT, padx=5)   

        self.search_result_label = tk.Label(self.window, text="******************** Search results ********************", font=("Helvetica", 14, "bold"))
        self.search_result_label.pack(pady=10)
        self.search_result_label_2 = tk.Label(self.window, text="Click on the title to view the full article.", font=("Helvetica", 10))
        self.search_result_label_2.pack(pady=0)
        
        self.search_results_text = scrolledtext.ScrolledText(self.window, width=100, height=30, wrap=tk.WORD)
        self.search_results_text.pack(pady=10)
        self.search_results_text.bind("<ButtonRelease-1>", self.show_selected_article)
                
        self.selected_title_entry = tk.Entry(self.window, width=80) 
        self.selected_title_entry.pack(pady=5)

    def search(self):
        query = self.query_entry.get()
        if query:
            self.show_search_results(query)
        else:
            messagebox.showinfo("Error", "Please enter a query.")
            
    def show_search_results(self, query):
        vector_model = VectorSpaceModel(self.documents)
        search_result, ranked_similarities = vector_model.search(query)       
        self.results = search_result
        self.search_results_text.delete("1.0", tk.END)
        
        if len(search_result) > 0:
            for idx in search_result[:100]:
                title = self.documents[idx]['title']
                date = self.documents[idx]['date']
                self.search_results_text.insert(tk.END, f"Title: {title}\nDate: {date}\n")
                keywords = extract_keywords(self.documents[idx]['article'])
                self.search_results_text.insert(tk.END, f"Keywords: {keywords}\n\n")
        else:
            self.search_results_text.insert(tk.END, "No matching documents found.")

            
    def read_selected_article(self):
        selected_title = self.selected_title_entry.get()
        if selected_title:
            for doc in self.documents:
                if doc['title'] == selected_title:
                    article = doc['article']
                    self.show_article_window(selected_title, article)
                    return
            messagebox.showinfo("Error", "Please click on a valid title from the search results.")
        else:
            messagebox.showinfo("Error", "Please click on a valid title from the search results.")
            
    def show_article_window(self, title, article):
        article_window = tk.Toplevel(self.window)
        article_window.title(title)
        article_window.geometry("800x600")  
        
        article_text = scrolledtext.ScrolledText(article_window, width=100, height=30, wrap=tk.WORD)
        article_text.pack(padx=10, pady=10)
        article_text.insert(tk.END, article)
        
        back_button_frame = tk.Frame(article_window)
        back_button_frame.pack(pady=10)        
        back_button = BackButton(back_button_frame, article_window.destroy)
        back_button.pack(side=tk.LEFT, padx=5)

    def show_selected_article(self, event):
        index = self.search_results_text.index(tk.CURRENT)
        line_number = int(index.split('.')[0])
        title_line = self.search_results_text.get(f"{line_number}.0", f"{line_number}.end")
        title = title_line.split("Title: ")[-1].split("  Date: ")[0]
        self.selected_title_entry.delete(0, tk.END)
        self.selected_title_entry.insert(0, title)
        self.read_selected_article()

    def close_window(self):
        self.window.destroy()

    def show_graph(self):
        graph_window = tk.Toplevel(self.window)
        graph_window.title("Social Event Visualization")
        graph_window.geometry("600x700")
        draw_graph(self.results, self.documents, graph_window)
