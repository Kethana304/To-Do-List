import json

TASKS_FILE = "tasks.json"
def load_tasks():
    try:
        with open(TASKS_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

def show_tasks(tasks):
    if not tasks:
        print("\n No tasks found!")
    else:
        print("\n Your Tasks:")
        for i, task in enumerate(tasks, 1):
            status = " Done" if task["done"] else " !!Pending"
            print(f"{i}. {task['title']} - {status}")

def add_task(tasks):
    title = input("Enter task: ")
    tasks.append({"title": title, "done": False})
    save_tasks(tasks)
    print("Task added!")

def mark_done(tasks):
    show_tasks(tasks)
    try:
        task_no = int(input("Enter task number to mark done: "))
        tasks[task_no - 1]["done"] = True
        save_tasks(tasks)
        print(" Task marked as done!")
    except (ValueError, IndexError):
        print(" Invalid choice!")

def delete_task(tasks):
    show_tasks(tasks)
    try:
        task_no = int(input("Enter task number to delete: "))
        tasks.pop(task_no - 1)
        save_tasks(tasks)
        print(" Task deleted!")
    except (ValueError, IndexError):
        print(" Invalid choice!")

def main():
    tasks = load_tasks()

    while True:
        print("\n=== TO-DO LIST MENU ===")
        print("1. Show Tasks")
        print("2. Add Task")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_done(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print(" Exiting... Have a productive day!")
            break
        else:
            print("" \
            " Invalid choice! Try again.")

if __name__ == "__main__":
    main()
