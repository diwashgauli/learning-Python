import csv

tasks = []

# Read tasks from todo.csv
try:
    with open('todo.csv', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Convert is_completed from string to boolean
            row['is_completed'] = row['is_completed'].lower() == 'true'
            tasks.append(row)
except FileNotFoundError:
    tasks = []

while True:
    print("\n1. Add Task")
    print("2. Remove Task")
    print("3. Mark as Complete")
    print("4. View Tasks")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        task_name = input("Enter your task: ").strip()
        if task_name:
            tasks.append({'task': task_name, 'is_completed': False})
        else:
            print("Task cannot be empty.")

    elif choice == 2:
        taskN = int(input("Enter task number to delete: "))
        if 0 < taskN <= len(tasks):
            tasks.pop(taskN - 1)
            print("Task removed.")
        else:
            print("Invalid task number.")

    elif choice == 3:
        taskN = int(input("Enter task number to mark as complete: "))
        if 0 < taskN <= len(tasks):
            if tasks[taskN - 1]['is_completed']:
                print("Task is already marked.")
            else:
                tasks[taskN - 1]['is_completed'] = True
                print("Task marked as completed.")
        else:
            print("Invalid task number.")

    elif choice == 4:
        if not tasks:
            print("No tasks available.")
        else:
            for i, task in enumerate(tasks):
                symbol = '\u2713' if task['is_completed'] else '\u2717'
                print(f"{i + 1}. {task['task']} {symbol}")

    elif choice == 5:
        with open('todo.csv', 'w', newline='') as file:
            fieldnames = ['task', 'is_completed']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            # convert boolean to string before writing
            for task in tasks:
                writer.writerow({
                    'task': task['task'],
                    'is_completed': str(task['is_completed'])
                })
        print("Thank you!")
        break

    else:
        print("Invalid choice.")

    input("Enter any key to continue...")
