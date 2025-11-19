import json
import os

TODO_FILE = "tasks.json"

def load_tasks():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r") as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(TODO_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

def show_tasks(tasks):
    if not tasks:
        print("\n✅ No tasks yet!\n")
        return
    print("\n📝 Your To-Do List:")
    for i, task in enumerate(tasks, start=1):
        status = "✔️" if task["done"] else "❌"
        print(f"{i}. {task['title']} [{status}]")
    print()

def add_task(tasks):
    title = input("Enter new task: ").strip()
    if title:
        tasks.append({"title": title, "done": False})
        save_tasks(tasks)
        print("✅ Task added!\n")
    else:
        print("⚠️ Task cannot be empty.\n")

def complete_task(tasks):
    show_tasks(tasks)
    try:
        num = int(input("Enter task number to mark as done: "))
        if 1 <= num <= len(tasks):
            tasks[num-1]["done"] = True
            save_tasks(tasks)
            print("🎉 Task marked as done!\n")
        else:
            print("⚠️ Invalid task number.\n")
    except ValueError:
        print("⚠️ Please enter a number.\n")

def delete_task(tasks):
    show_tasks(tasks)
    try:
        num = int(input("Enter task number to delete: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num-1)
            save_tasks(tasks)
            print(f"🗑️ Deleted task: {removed['title']}\n")
        else:
            print("⚠️ Invalid task number.\n")
    except ValueError:
        print("⚠️ Please enter a number.\n")

def main():
    tasks = load_tasks()
    while True:
        print("===== TO-DO LIST APP =====")
        print("1️. Show tasks")
        print("2️. Add task")
        print("3️. Complete task")
        print("4️. Delete task")
        print("5️. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("👋 Goodbye!")
            break
        else:
            print("⚠️ Invalid option, try again.\n")

if __name__ == "__main__":
    main()
