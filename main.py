"""PYTHON TODO LIST APP"""

# Empty list to store tasks
tasks = []

# Function 1: Show tasks
def show_task():
    if len(tasks) == 0:
        print("No task available.")
    else:
        for i in range(len(tasks)):
            print(f"{i + 1}.  {tasks[i]}")

def add_task():
    task = input("Enter a new task.")
    tasks.append(task)
    print("Task added successfully.")
    show_task()
