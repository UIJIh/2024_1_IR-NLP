import sys
sys.path.append('..')
from utils.buttons import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk

def draw_graph(search_result, documents, graph_window):
    if search_result is None:
        return
    date_ranges = ['Jan 1-15', 'Jan 16-31', 'Feb 1-15', 'Feb 16-29', 'Mar 1-15', 'Mar 16-31', 'Apr 1-15']
    counts = [0] * len(date_ranges)

    for doc in search_result:
        date = int(documents[doc]['date'][8:10])  
        month = int(documents[doc]['date'][5:7])  

        if month == 1:
            if 1 <= date <= 15:
                counts[0] += 1
            elif 16 <= date <= 31:
                counts[1] += 1
        elif month == 2:
            if 1 <= date <= 15:
                counts[2] += 1
            elif 16 <= date <= 29:
                counts[3] += 1
        elif month == 3:
            if 1 <= date <= 15:
                counts[4] += 1
            elif 16 <= date <= 31:
                counts[5] += 1
        elif month == 4:
            if 1 <= date <= 15:
                counts[6] += 1
                
    total_articles = sum(counts)    

    fig, ax = plt.subplots(figsize=(4, 3))
    ax.bar(date_ranges, counts, color='skyblue')
    ax.set_title(f'Article Distribution from January to April\nTotal Articles: {total_articles}')
    ax.set_xlabel('Date Range')
    ax.set_ylabel('Number of Articles')
    ax.set_xlabel('Date Range')
    ax.set_ylabel('Number of Articles')
    ax.set_xticks(range(len(date_ranges)))  
    ax.set_xticklabels(date_ranges, rotation=45, ha='right')

    canvas = FigureCanvasTkAgg(fig, master=graph_window)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
   
    close_button = ExitButton(graph_window, command=graph_window.destroy)
    close_button.pack(side=tk.BOTTOM, pady=5)
    graph_window.protocol("WM_DELETE_WINDOW", graph_window.quit)
    graph_window.mainloop()