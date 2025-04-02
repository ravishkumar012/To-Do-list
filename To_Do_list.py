tasks=[]
def add_task(tasks):
    task=input("enter a new task!\t")
    tasks.append(task)
    print(f"Task '{task}' added sucessfully!")
def remove_task(tasks):
    view_task(tasks)
    if not tasks:
        print("No tasks to delete!")
        return
    else:
        task_index=int(input("enter a task index to delete!\t"))
        for task in range(len(tasks)):
            if task==task_index:
                tasks.pop(task_index-1)
                print(f"Task at index {task_index} deleted successfully!")
                return
def view_task(tasks):
    if not tasks:
        print("No tasks to view!")
        return
    else:
        print("Tasks:")
        for task in range(len(tasks)):
            print(f"{task+1}. {tasks[task]}")
        print()
        return
def edit_task(tasks):
    view_task(tasks)
    if not tasks:
        print("No task found!")
        return
    else:
        task_index=int(input("enter a task index  to update!"))
        for task in range(len(tasks)):
            if task_index==task:
                new_task=input("enter new task!\t")
                tasks[task_index-1]=new_task
                print(f"Task at index {task_index} updated successfully!")
                return

def main():
    while True:
        print("\tTo Do List!")
        print("1. Add a task")
        print("2. Remove a task")
        print("3. View tasks")
        print("4. Edit a task")
        print("5. Exit")
        choice=int(input("Enter your choice: "))
        if choice==1:
            add_task(tasks)
        elif choice==2:
            remove_task(tasks)
        elif choice==3:
            view_task(tasks)
        elif choice==4:
            edit_task(tasks)
        elif choice==5:
            print("Exit!")
            break
        else:
            print("Invalid choice!")

if __name__=="__main__":
    main()


