### 🔹 2. To-Do List (w/ File Handling)

def add_task(task):
    with open("todo.txt", "a") as file:
        file.write(task + "\n")
    print("✅ Task added.")

def view_tasks():
    try:
        with open("todo.txt", "r") as file:
            tasks = file.readlines()
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task.strip()}")
    except FileNotFoundError:
        print("📭 No tasks yet.")

# Simple CLI
while True:
    print("\n--- To-Do List ---")
    print("1. Add Task\n2. View Tasks\n3. Exit")
    choice = input("Choose: ")

    if choice == "1":
        task = input("Enter task: ")
        add_task(task)
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        break
    else:
        print("⚠️ Invalid option")
