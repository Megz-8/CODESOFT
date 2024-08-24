import tkinter as tk
from tkinter import messagebox

class ToDoList:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.tasks = []

        # Create GUI elements
        self.task_entry = tk.Entry(self.root, width=40)
        self.task_entry.grid(row=0, column=0)

        self.add_task_button = tk.Button(self.root, text="Add Task", command=self.add_task)
        self.add_task_button.grid(row=0, column=1)

        self.task_list = tk.Listbox(self.root, width=40)
        self.task_list.grid(row=1, column=0, columnspan=2)

        self.delete_task_button = tk.Button(self.root, text="Delete Task", command=self.delete_task)
        self.delete_task_button.grid(row=2, column=0, columnspan=2)

    def add_task(self):
        task = self.task_entry.get()
        if task != "":
            self.tasks.append(task)
            self.task_list.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)

    def delete_task(self):
        try:
            task_index = self.task_list.curselection()[0]
            self.task_list.delete(task_index)
            self.tasks.pop(task_index)
        except IndexError:
            messagebox.showwarning("Error", "Select a task to delete")

if __name__ == "__main__":
    root = tk.Tk()
    todo_list = ToDoList(root)
    root.mainloop()

