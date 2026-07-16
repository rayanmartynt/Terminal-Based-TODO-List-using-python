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