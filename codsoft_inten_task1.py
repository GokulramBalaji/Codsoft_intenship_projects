task()
def add_task(task):
    task.append(task)
    print("Task'{task}' added tok the list")

def list_tasks():
    if not tasks:
        print("There is no task in the list")
        return
    for index,task in enumerate(tasks):
        print("{index+1}.{task}")
    def main():
        print("To do list application")
        print("1.Add task")
        print("2.List Tasks")
        print("3.Exit")
        choice=input("Enter your choice(1-3):")

        if choice=="1":
            task=input("Enter the new task")
            add_task(task)
        elif choice=="2":
            list_tasks()
        elif choice=="3":
            break
        else:
            print("Invalid choice please enter a valid one")



    
        
        
