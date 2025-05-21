todo = []

while True:
    print("\n--- Simple To-Do List ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == '1':
        task = input("Enter a task: ")
        todo.append(task)
        print(f"Added: {task}")
    elif choice == '2':
        print("\nYour Tasks:")
        for i, task in enumerate(todo, 1):
            print(f"{i}. {task}")
    elif choice == '3':
        print("Exited!")
        break
    else:
        print("Invalid choice.")
