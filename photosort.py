from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
import os
from datetime import datetime

def choose_folder():
    dir_path = filedialog.askdirectory()
    e_path.delete(0, END)
    e_path.insert(0, dir_path)


def start_sort():
    cur_path = e_path.get()
    if cur_path:
        for folder, subfolders, files in os.walk(cur_path):
            for file in files:
                path = os.path.join(folder, file)
                mod_time = os.path.getmtime(path)
                date = datetime.fromtimestamp(mod_time)
                date = date.strftime("%Y-%m-%d") # YYYY-MM-DD
                date_folder = os.path.join(cur_path, date)
                if not os.path.exists(date_folder):
                    os.mkdir(date_folder)
                os.rename(path, os.path.join(date_folder, file))
        messagebox.showinfo("Success", "Sort is complete successfully")
        e_path.delete(0, END)
    else:
        messagebox.showwarning("Warning", "Choose the folder with photos")


root = Tk()
root.title("PhotoSort")
root.geometry("500x150+800+300")

styles = ttk.Style()
styles.configure("my.TButton", font=("Helvetica", 15))

frame = Frame(root, bg="#56adff", bd=5)
frame.pack(padx=10, pady=10, fill=X)

e_path = ttk.Entry(frame)
e_path.pack(side=LEFT, ipady=2, expand=True, fill=X)

btn_dialog = ttk.Button(frame, text="Choose folder", command=choose_folder)
btn_dialog.pack(side=LEFT, padx=5)

btn_start = ttk.Button(root, text="Start", style="my.TButton", command=start_sort)
btn_start.pack(fill=X, padx=10)

root.mainloop()