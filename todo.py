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

def add_task():
    title = input("Task title (or 'q' to cancel): ").strip()
    if title.lower() == 'q':
        print("Cancelled.")
        return
    tasks = load_tasks()
    tasks.append({"title": title, "done": False})
    save_tasks(tasks)
    print(f"Added: {title}")

def list_tasks(tasks):
    if not tasks:
        print("No tasks yet!")
        return False
    for i, task in enumerate(tasks):
        status = "✓" if task["done"] else "✗"
        print(f"{i + 1}. [{status}] {task['title']}")
    return True

def pick_task(prompt):
    """Show tasks and prompt the user to pick one. Returns index or None if cancelled."""
    tasks = load_tasks()
    if not list_tasks(tasks):
        return None, None

    raw = input(f"{prompt} (or 'q' to cancel): ").strip()
    if raw.lower() == 'q':
        print("Cancelled.")
        return None, None

    if not raw.isdigit():
        print("Invalid input, please enter a number.")
        return None, None

    i = int(raw) - 1
    if i < 0 or i >= len(tasks):
        print(f"Please enter a number between 1 and {len(tasks)}.")
        return None, None

    return i, tasks

def complete_task():
    i, tasks = pick_task("Task number to complete")
    if i is None:
        return
    if tasks[i]["done"]:
        print(f"Already completed: {tasks[i]['title']}")
        return
    tasks[i]["done"] = True
    save_tasks(tasks)
    print(f"Completed: {tasks[i]['title']}")

def delete_task():
    i, tasks = pick_task("Task number to delete")
    if i is None:
        return
    removed = tasks.pop(i)
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
            tasks = load_tasks()
            list_tasks(tasks)
        elif choice == "2":
            add_task()
        elif choice == "3":
            complete_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()

