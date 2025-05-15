# tasks = [
#     {'task': 'goto market',    'is_completed': True},  #dictionary 1
#     {'task': 'learn python',   'is_completed': False}, #dictionary 2
#     {'task': 'call mom',       'is_completed': False}, #dictionary 3
# ]
import json
tasks = []
with open ('todo.json') as file:
    tasks=json.load(file)

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
        for i, task in enumerate(tasks):
            symbol = '\u2713' if task['is_completed'] else '\u2717'
            print(f"{i + 1}. {task['task']} {symbol}")

    elif choice == 5:
        with open('todo.json','w') as file:
            json.dump(tasks,file,indent=4)
        print("Thank you!")
        break

    else:
        print("Invalid choice.")

    input("Enter any key to continue...")
