import os

TASK_FILE = 'tasks.txt'

def load_tasks():
    if not os.path.exists(TASK_FILE):
        return []
    with open(TASK_FILE, 'r') as file:
        tasks = file.readlines()
    return [task.strip() for task in tasks]

def save_tasks(tasks):
    with open(TASK_FILE, 'w') as file:
        for task in tasks:
            file.write(task + '\n')

def add_task(tasks):
    task = input("Enter a new task: ")
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task '{task}' added.")

def remove_task(tasks):
    task = input("Enter the task to remove: ")
    if task in tasks:
        tasks.remove(task)
        save_tasks(tasks)
        print(f"Task '{task}' removed.")
    else:
        print(f"Task '{task}' not found.")

def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
    else:
        print("Tasks:")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")

def main():
    tasks = load_tasks()
    while True:
        print("=========== Task List Manager ===========")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. View Tasks")
        print("4. Exit")
        print("=========================================")
        choice = input("Choose an option: ")
        print("===========")
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            remove_task(tasks)
        elif choice == '3':
            view_tasks(tasks)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")
        print("===========")

if __name__ == "__main__":
    main()
