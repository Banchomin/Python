from tkinter import *
import pickle
import tkinter.messagebox


def entertask():
    task = entry_task.get()
    if task:
        listbox_task.insert(END, task)
        entry_task.delete(0, END)
    else:
        tkinter.messagebox.showwarning(title="Warning", message="Please enter a task.")


def deletetask():
    try:
        task_index = listbox_task.curselection()[0]
        listbox_task.delete(task_index)
    except IndexError:
        tkinter.messagebox.showwarning(title="Warning", message="Please select a task.")


def markcompleted():
    try:
        task_index = listbox_task.curselection()[0]
        task_text = listbox_task.get(task_index)
        completed_text = f"{task_text} (Completed)"
        listbox_task.delete(task_index)
        listbox_task.insert(task_index, completed_text)
    except IndexError:
        tkinter.messagebox.showwarning(title="Warning", message="Please select a task.")


# creating the initial window
window = Tk()

# giving a title
window.title("DataFlair Python To-Do List APP")

# creating a frame to hold the task list
frame_task = Frame(window)
frame_task.pack()

# creating a listbox to display the task list
listbox_task = Listbox(
    frame_task, bg="black", fg="white", height=15, width=50, font="Helvetica"
)
listbox_task.pack(side=LEFT)

# creating an entry box and a button to add tasks
entry_task = Entry(window, width=50)
entry_task.pack(pady=3)

entry_button = Button(window, text="Add task", width=50, command=entertask)
entry_button.pack(pady=3)

# creating a button to delete tasks
delete_button = Button(
    window, text="Delete selected task", width=50, command=deletetask
)
delete_button.pack(pady=3)

# creating a button to mark tasks as completed
mark_button = Button(window, text="Mark as completed", width=50, command=markcompleted)
mark_button.pack(pady=3)

# loading the saved tasks from a file
try:
    with open("tasks.pkl", "rb") as f:
        saved_tasks = pickle.load(f)
        for task in saved_tasks:
            listbox_task.insert(END, task)
except FileNotFoundError:
    pass


# saving the tasks to a file when the window is closed
def on_closing():
    tasks = listbox_task.get(0, END)
    with open("tasks.pkl", "wb") as f:
        pickle.dump(tasks, f)
    window.destroy()


window.protocol("WM_DELETE_WINDOW", on_closing)

window.mainloop()
