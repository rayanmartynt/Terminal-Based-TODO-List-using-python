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

# Function 2: Add task
def add_task():
    task = input("Enter a new task.")
    tasks.append(task)
    print("Task added successfully.")
    show_task()

# Function 3: Remove task
def remove_task():
    if len(tasks) > 0:
        number = int(input("Enter the number of the task you want to remove:"))
        if 1 <= number <= len(tasks):
            removed = tasks.pop(number - 1)
            print(f"{removed} removed")
        else:
            print("Invalid task number.")
