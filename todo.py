import json
import os

FILE = "tasks.json"

def load_tasks():
    if not os.path.exists(FILE):
        return []
    with open(FILE, "r") as f:
        return json.load(f)

def save_tasks(tasks):
    with open(FILE, "w") as f:
        json.dump(tasks, f, indent=2)

def add_task(title):
    tasks = load_tasks()
    tasks.append({"title": title, "done": False})
    save_tasks(tasks)
    print(f"Added: {title}")

def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks yet!")
        return
    for i, task in enumerate(tasks):
        status = "✓" if task["done"] else "✗"
        print(f"{i + 1}. [{status}] {task['title']}")

def complete_task(index):
    tasks = load_tasks()
    tasks[index]["done"] = True
    save_tasks(tasks)
    print(f"Completed: {tasks[index]['title']}")

def delete_task(index):
    tasks = load_tasks()
    removed = tasks.pop(index)
    save_tasks(tasks)
    print(f"Deleted: {removed['title']}")

def main():
    while True:
        print("\n--- To-Do List ---")
        print("1. List tasks")
        print("2. Add task")
        print("3. Complete task")
        print("4. Delete task")
        print("5. Quit")

        choice = input("\nChoice: ").strip()

        if choice == "1":
            list_tasks()
        elif choice == "2":
            title = input("Task title: ").strip()
            add_task(title)
        elif choice == "3":
            list_tasks()
            i = int(input("Task number to complete: ")) - 1
            complete_task(i)
        elif choice == "4":
            list_tasks()
            i = int(input("Task number to delete: ")) - 1
            delete_task(i)
        elif choice == "5":
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
