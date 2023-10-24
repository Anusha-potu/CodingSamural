import tkinter as tk

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)

def remove_task():
    selected_task = listbox.curselection()
    if selected_task:
        listbox.delete(selected_task)

# Create the main application window
app = tk.Tk()
app.title("To-Do List Application")
app.geometry("700x500")
app.configure(bg="Pink")  # Set background color

# Create a label
label = tk.Label(app, text="Enter your task:", bg="orange")
label.pack(pady=10)

# Create an entry widget for task input
entry = tk.Entry(app, width=40)
entry.pack(pady=10)

# Create a button to add tasks
add_button = tk.Button(app, text="Add Task", command=add_task, bg="green")
add_button.pack(pady=5)

# Create a listbox to display tasks
listbox = tk.Listbox(app, selectbackground="dark blue")
listbox.pack(pady=10)

# Create a button to remove selected tasks
remove_button = tk.Button(app, text="Remove Task", command=remove_task, bg="red")
remove_button.pack(pady=5)

app.mainloop()


