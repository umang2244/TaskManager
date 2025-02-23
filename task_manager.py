import tkinter as tk
from tkinter import messagebox

class TaskManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Task Manager")
        self.root.geometry("400x500")
        
        # Task list
        self.tasks = []

        # UI Components
        # Title
        self.title_label = tk.Label(root, text="Task Manager", font=("Arial", 16, "bold"))
        self.title_label.pack(pady=10)

        # Task entry
        self.task_entry = tk.Entry(root, width=30)
        self.task_entry.pack(pady=5)
        self.task_entry.focus()

        # Add task button
        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.pack(pady=5)

        # Task listbox
        self.task_listbox = tk.Listbox(root, width=40, height=15)
        self.task_listbox.pack(pady=10)

        # Complete and Delete buttons
        self.complete_button = tk.Button(root, text="Complete Task", command=self.complete_task)
        self.complete_button.pack(pady=5)

        self.delete_button = tk.Button(root, text="Delete Task", command=self.delete_task)
        self.delete_button.pack(pady=5)

        # Exit button
        self.exit_button = tk.Button(root, text="Exit", command=root.quit)
        self.exit_button.pack(pady=5)

        # Bind Enter key to add task
        self.root.bind('<Return>', lambda event: self.add_task())

    def add_task(self):
        task = self.task_entry.get().strip()
        if task:
            self.tasks.append({"task": task, "completed": False})
            self.update_task_list()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please enter a task!")

    def update_task_list(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            status = "✓" if task["completed"] else "✗"
            self.task_listbox.insert(tk.END, f"{task['task']} [{status}]")

    def complete_task(self):
        try:
            index = self.task_listbox.curselection()[0]
            self.tasks[index]["completed"] = True
            self.update_task_list()
        except IndexError:
            messagebox.showwarning("Selection Error", "Please select a task to complete!")

    def delete_task(self):
        try:
            index = self.task_listbox.curselection()[0]
            del self.tasks[index]
            self.update_task_list()
        except IndexError:
            messagebox.showwarning("Selection Error", "Please select a task to delete!")

def main():
    root = tk.Tk()
    app = TaskManagerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()