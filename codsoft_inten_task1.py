asks = []

def add_task(task):
    tasks.append(task)
    print(f"Task '{task}' added to the list.")

def list_tasks():
    if not tasks:
        print("There are no tasks in the list.")
        return
    print("Your to-do list:")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")

def main():
    print("To-Do List Application")
    while True:
        print("\nMenu:")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            task = input("Enter the new task: ")
            add_task(task)
        elif choice == '2':
            list_tasks()
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")
main()
