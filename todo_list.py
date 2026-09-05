def manage_todos():
    todos = []
    
    while True:
        print("\n--- To-Do List ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ")
        
        if choice == "1":
            if not todos:
                print("Your to-do list is empty.")
            else:
                print("\nCurrent Tasks:")
                for i, task in enumerate(todos, 1):
                    print(f"{i}. {task}")
        elif choice == "2":
            task = input("Enter the task description: ").strip()
            if task:
                todos.append(task)
                print(f"Added: '{task}'")
        elif choice == "3":
            if not todos:
                print("No tasks to remove.")
                continue
            try:
                index = int(input("Enter task number to remove: ")) - 1
                if 0 <= index < len(todos):
                    removed = todos.pop(index)
                    print(f"Removed: '{removed}'")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid integer.")
        elif choice == "4":
            print("Exiting To-Do Manager.")
            break
        else:
            print("Invalid choice. Please select between 1 and 4.")

if __name__ == "__main__":
    manage_todos()
