# Simple To-Do List (todo.py)

tasks = []

def show_menu():
    print("\n--- To-Do List ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exit")

while True:
    show_menu()
    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        task = input("Enter task: ")
        tasks.append({"task": task, "done": False})
        print("✅ Task added!")

    elif choice == '2':
        if not tasks:
            print("No tasks yet!")
        else:
            print("\nYour Tasks:")
            for i, t in enumerate(tasks, 1):
                status = "✅ Done" if t["done"] else "❌ Not Done"
                print(f"{i}. {t['task']} - {status}")

    elif choice == '3':
        num = int(input("Enter task number to mark done: "))
        if 1 <= num <= len(tasks):
            tasks[num-1]["done"] = True
            print("✔ Task marked as done!")
        else:
            print("Invalid task number!")

    elif choice == '4':
        num = int(input("Enter task number to delete: "))
        if 1 <= num <= len(tasks):
            tasks.pop(num-1)
            print("🗑 Task deleted!")
        else:
            print("Invalid task number!")

    elif choice == '5':
        print("Goodbye! 👋")
        break

    else:
        print("Invalid choice! Try again.")

print("this is a new feature (checkbox)")