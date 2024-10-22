import requests
import tkinter as tk
from tkinter import ttk

def fetch_ip_info(url):
    try:
        response = requests.get(url)
        data = response.json()
        return data
    except Exception as e:
        return {'error': str(e)}

def update_ui(url, label):
    data = fetch_ip_info(url)
    if 'error' in data:
        label.config(text=f"Error: {data['error']}")
    else:
        label.config(text=(
            f"IP Address: {data.get('ip', 'N/A')}\n"
            f"City: {data.get('city', 'N/A')}\n"
            f"Region: {data.get('region', 'N/A')}\n"
            f"Country: {data.get('country_name', 'N/A')}\n"
            f"ISP: {data.get('org', 'N/A')}"
        ))

def show_info_page():
    clear_frame()
    
    title_label = ttk.Label(frame, text="T39's PC Information", font=('Helvetica', 18, 'bold'))
    title_label.grid(row=0, column=0, pady=(20, 10), sticky="nsew")

    global ip_info_label
    ip_info_label = ttk.Label(frame, text="Loading...", justify="center", font=('Helvetica', 14))
    ip_info_label.grid(row=1, column=0, sticky="nsew")

    update_ui('https://ipapi.co/json/', ip_info_label)

    back_button.grid(row=5, column=0, pady=(10, 20), sticky="nsew")

def show_start_page():
    clear_frame()
    
    header_label = ttk.Label(frame, text="Team 39's Application", font=('Helvetica', 24, 'bold'))
    header_label.grid(row=0, column=0, pady=(40, 20), sticky="nsew")

    subHeader_label = ttk.Label(frame, text="IPv4/IPv6 Application", font=('Helvetica', 18))
    subHeader_label.grid(row=1, column=0, pady=(10, 20), sticky="nsew")

    start_button = ttk.Button(frame, text="Start", command=show_info_page)
    start_button.grid(row=2, column=0, pady=(10, 20), sticky="nsew")
    
    start_button.config(width=15)

    back_button.grid_remove()

def clear_frame():
    for widget in frame.winfo_children():
        if widget != back_button:
            widget.destroy()

root = tk.Tk()
root.title("IP Address Info")
root.geometry("800x600")
root.resizable(True, True)
root.configure(bg="#f4f4f4")

frame = ttk.Frame(root, padding="20", relief="raised", borderwidth=2)
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
frame.configure(style='TFrame')

frame.grid_rowconfigure(0, weight=1)
frame.grid_rowconfigure(1, weight=1)
frame.grid_rowconfigure(2, weight=1)
frame.grid_columnconfigure(0, weight=1)

style = ttk.Style()
style.configure('TButton', font=('Helvetica', 12), padding=10)

back_button = ttk.Button(frame, text="Back", command=show_start_page)

show_start_page()
root.mainloop()
