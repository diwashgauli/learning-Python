tasks = []
status = []

while True:
    print("\n1. Add Task")
    print("2. Remove Task")
    print("3. Mark as Complete")
    print("4. View Tasks")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        task = input("Enter your task: ").strip()
        if task:
            tasks.append(task)
            status.append(False)
        else:
            print("Task cannot be empty.")

    elif choice == 2:
        taskN = int(input("Enter task number to delete: "))
        if 0 < taskN <= len(tasks):
            tasks.pop(taskN - 1)
            status.pop(taskN - 1)
            print("Task removed.")
        else:
            print("Invalid task number.")

    elif choice == 3:
        taskN = int(input("Enter task number to mark as complete: "))
        if 0 < taskN <= len(tasks):
            if status[taskN - 1]:
                print("Task is already marked.")
            else:
                status[taskN - 1] = True
                print("Task marked as completed.")
        else:
            print("Invalid task number.")

    elif choice == 4:
        if not tasks:
            print("No tasks available.")
        for i in range(len(tasks)):
            symbol = '\u2713' if status[i] else '\u2717'
            print(f"{i + 1}. {tasks[i]} {symbol}")

    elif choice == 5:
        print("Thank you!")
        break

    else:
        print("Invalid choice.")

    input("Enter any key to continue...")
