import tkinter as tk
from tkinter import simpledialog
from tkinter import ttk
import time

def get_number():
    root.withdraw()  # Hide the main window
    number = simpledialog.askinteger("Enter a Number", "Enter a number you're thinking about:")
    return number

def center_window(window):
    window.update_idletasks()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    window_width = window.winfo_width()
    window_height = window.winfo_height()
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2
    window.geometry(f"+{x}+{y}")

def show_loading_bar():
    loading_window = tk.Toplevel(root)
    loading_window.title("Loading Bar")
    loading_window.geometry("300x100")
    center_window(loading_window)

    label = tk.Label(loading_window, text="Loading...")
    label.pack()

    progress = tk.DoubleVar()
    progress.set(0)
    
    style = ttk.Style()
    style.configure("TProgressbar", thickness=20)
    progress_bar = ttk.Progressbar(loading_window, variable=progress, maximum=100, style="TProgressbar", mode="determinate")
    progress_bar.pack()

    descriptions = ["Reading your mind...", "Analyzing brainwaves...", "Processing...", "Almost there...", "Coming up with the solution..."]
    
    for i in range(5):
        description = descriptions[i]
        label.config(text=f"{description} ({i + 1}/5)")
        for j in range(20):
            progress.set(i * 20 + j)
            loading_window.update()
            time.sleep(0.05)  # Adjust the sleep time for smoother progress

    loading_window.destroy()

def show_result(number):
    result_window = tk.Toplevel(root)
    result_window.title("Result")
    result_window.geometry("300x100")
    center_window(result_window)

    label = tk.Label(result_window, text=f"You were thinking about the number: {number}")
    label.pack()

    result_window.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # Hide the main window initially

    number = get_number()
    if number is not None:
        show_loading_bar()
        show_result(number)

    root.mainloop()
