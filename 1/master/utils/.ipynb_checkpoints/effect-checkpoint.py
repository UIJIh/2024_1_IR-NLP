import random

def flash_text(button):
    color = random.choice(['red', 'green', 'blue', 'purple'])
    button.config(fg=color)
    button.after(500, lambda: flash_text(button)) 