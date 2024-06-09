import sys

tasks = []

def add_task(task):
    tasks.append(task)
    print("Task ",task,"added.")

def view_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        for i, task in enumerate(tasks, start=1):
            print(i , task)

def delete_task(task_number):
    try:
        task = tasks.pop(task_number - 1)
        print("Task ",task,"deleted.")
    except IndexError:
        print("Invalid task number.")

def show_help():
    print("Commands:")
    print("add <task> - Add a new task")
    print("view - View all tasks")
    print("delete <task_number> - Delete a task")
    print("exit - Exit the application")

def main():
    print("Welcome to the To-Do List application!")
    show_help()

    while True:
        command = input("> ").strip().split(maxsplit=1)
        if not command:
            continue

        action = command[0].lower()
        if action == "add" and len(command) > 1:
            add_task(command[1])
        elif action == "view":
            view_tasks()
        elif action == "delete" and len(command) > 1:
            if command[1].isdigit():
                delete_task(int(command[1]))
            else:
                print("Please enter a valid task number.")
        elif action == "exit":
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Unknown command.")
            show_help()

if __name__ == "__main__":
    main()
