import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task:
        tasks_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task!")

def remove_task():
    try:
        selected_task = tasks_listbox.curselection()
        tasks_listbox.delete(selected_task)
    except:
        messagebox.showwarning("Selection Error", "Please select a task to remove!")

def mark_complete():
    try:
        selected_task_index = tasks_listbox.curselection()
        task = tasks_listbox.get(selected_task_index)
        tasks_listbox.delete(selected_task_index)
        tasks_listbox.insert(tk.END, f"{task} ✅")
    except:
        messagebox.showwarning("Selection Error", "Please select a task to mark as complete!")

def clear_all():
    tasks_listbox.delete(0, tk.END)

# Initialize GUI
root = tk.Tk()
root.title("To-Do List App")

# Input for new task
task_entry = tk.Entry(root, width=35, font=("Arial", 14))
task_entry.grid(row=0, column=0, padx=10, pady=10)

# Buttons
add_button = tk.Button(root, text="Add Task", width=15, command=add_task)
add_button.grid(row=0, column=1, padx=10)

remove_button = tk.Button(root, text="Remove Task", width=15, command=remove_task)
remove_button.grid(row=1, column=1, padx=10)

complete_button = tk.Button(root, text="Mark Complete", width=15, command=mark_complete)
complete_button.grid(row=2, column=1, padx=10)

clear_button = tk.Button(root, text="Clear All", width=15, command=clear_all)
clear_button.grid(row=3, column=1, padx=10)

# Listbox to display tasks
tasks_listbox = tk.Listbox(root, width=50, height=15, font=("Arial", 14))
tasks_listbox.grid(row=1, column=0, rowspan=3, padx=10, pady=10)

# Run the application
root.mainloop()
import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task:
        tasks_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task!")

def remove_task():
    try:
        selected_task = tasks_listbox.curselection()
        tasks_listbox.delete(selected_task)
    except:
        messagebox.showwarning("Selection Error", "Please select a task to remove!")

def mark_complete():
    try:
        selected_task_index = tasks_listbox.curselection()
        task = tasks_listbox.get(selected_task_index)
        tasks_listbox.delete(selected_task_index)
        tasks_listbox.insert(tk.END, f"{task} ✅")
    except:
        messagebox.showwarning("Selection Error", "Please select a task to mark as complete!")

def clear_all():
    tasks_listbox.delete(0, tk.END)

# Initialize GUI
root = tk.Tk()
root.title("To-Do List App")

# Input for new task
task_entry = tk.Entry(root, width=35, font=("Arial", 14))
task_entry.grid(row=0, column=0, padx=10, pady=10)

# Buttons
add_button = tk.Button(root, text="Add Task", width=15, command=add_task)
add_button.grid(row=0, column=1, padx=10)

remove_button = tk.Button(root, text="Remove Task", width=15, command=remove_task)
remove_button.grid(row=1, column=1, padx=10)

complete_button = tk.Button(root, text="Mark Complete", width=15, command=mark_complete)
complete_button.grid(row=2, column=1, padx=10)

clear_button = tk.Button(root, text="Clear All", width=15, command=clear_all)
clear_button.grid(row=3, column=1, padx=10)

# Listbox to display tasks
tasks_listbox = tk.Listbox(root, width=50, height=15, font=("Arial", 14))
tasks_listbox.grid(row=1, column=0, rowspan=3, padx=10, pady=10)

# Run the application
root.mainloop()
