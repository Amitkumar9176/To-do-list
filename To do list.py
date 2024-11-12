import json
import os

# File to store the to-do list
TODO_FILE = "todo_list.json"

# Load tasks from file if it exists
def load_tasks():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r") as file:
            return json.load(file)
    return []

# Save tasks to file
def save_tasks(tasks):
    with open(TODO_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

# Display all tasks
def view_tasks(tasks):
    if not tasks:
        print("No tasks in the list.")
        return
    for i, task in enumerate(tasks, start=1):
        status = "✓" if task["completed"] else "✗"
        print(f"{i}. [{status}] {task['text']}")

# Add a new task
def add_task(tasks):
    task_text = input("Enter the new task: ").strip()
    if task_text:
        tasks.append({"text": task_text, "completed": False})
        print("Task added.")
    else:
        print("Task cannot be empty.")

# Mark a task as complete or incomplete
def toggle_task(tasks):
    view_tasks(tasks)
    try:
        task_num = int(input("Enter the task number to toggle: "))
        if 1 <= task_num <= len(tasks):
            tasks[task_num - 1]["completed"] = not tasks[task_num - 1]["completed"]
            print("Task status updated.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Delete a task
def delete_task(tasks):
    view_tasks(tasks)
    try:
        task_num = int(input("Enter the task number to delete: "))
        if 1 <= task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            print(f"Deleted task: {removed_task['text']}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Main function to run the To-Do List App
def main():
    tasks = load_tasks()

    while True:
        print("\nTo-Do List App")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Toggle Task Completion")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option: ").strip()
        
        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            toggle_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print("Tasks saved. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()