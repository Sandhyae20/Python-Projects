# set up your environment

#import tkinter
import tkinter as tk
from tkinter import messagebox

## create the main application window
root = tk.Tk()
root.title("To-Do list")

#define functions for task managemnt

def add_task():
    task=task_entry.get()                        # Get the text from the entry widget
    if task.strip:                               # Check if the task is not empty
        task.listbox.insert(tk.END, task)        # Insert the task into the Listbox
        task_entry.delete(0,tk.END)              # Clear the entry widget
        
    else:
        messagebox.showwarning("Warning!  You must enter a task.")

def remove_task():
    try:
        task_index =task.curselection()[0]
        task.delete(task_index)
    except:
        messagebox.showwarning("Warning! you must select task to remove.")


def mark_task():
    try:
        task_index = task.curselection()[0]
        task = task.get(task_index)
        task.delete(task_index)
        task.insert(tk.END, task + " (Done)")
    except:
        messagebox.showwarning("Warning", "You must select a task to mark as done.")
          
          
# Set up the GUI Layout 

task = tk.Listbox(root, width=50, height=10)
task.pack(pady=10)

task_entry = tk.Entry(root, width=50)
task_entry.pack(pady=10)

add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack(pady=5)

remove_button = tk.Button(root, text="Remove Task", command=remove_task)
remove_button.pack(pady=5)

mark_button = tk.Button(root, text="Mark as Done", command=mark_task)
mark_button.pack(pady=5)


# Main Loop

root.mainloop()

