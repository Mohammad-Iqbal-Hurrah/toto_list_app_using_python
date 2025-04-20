"""Day 2 of 100 days pyhton mini projects 
Build a todo app using python capable of:
1. Adding new task
2. View all tasks
3. Mark as done 
4. Delete task
5. View Completed tasks
6. Save/Load from file"""
# Author: "Mohammad Iqbal Hurrah"
# Date: "20-April-2025"
# Day: Sunday    
tasks = []
comp_list = []
all_tasks = tasks + comp_list
def show():
    print("||***************************************** || My ToDo List App || *********************************||")
    print("""    1. Add a task
    2. View all tasks
    3. Delete a  task
    4. Mark task as done
    5. View completed tasks
    6. view pending tasks
    7. Exit""")
def add_task(): # Add a task to the list
    task = input("Enter your task: ")
    tasks.append(task)
    return "Task added successfully."
def view_tasks():   # View all tasks
    # global all_tasks
    all_tasks = tasks + comp_list
    new_list = []
    if len(all_tasks) != 0:
        print("Your tasks are: ")
        for item in all_tasks:
            if item not in new_list:
                new_list.append(item)
        counter = 1
        for item in new_list:
            print(counter, item.capitalize())
            counter += 1
    else:
        print("No tasks found.")
def delete_task():  # Delete a task from the list
    # global all_tasks
    all_tasks = tasks + comp_list
    if len(all_tasks) == 0:
        return "No tasks found to delete.", ""
    else:
        task = input("Enter the task you want to delete: ").lower()
        if task in tasks:
            tasks.remove(task)  # Remove from tasks list
            return "Task deleted successfully.", task
        elif task in comp_list:
            comp_list.remove(task)  # Remove from completed tasks list
            return "Task deleted successfully.", task
        else:
            return "Task not found in the tasks list.", ""
def done():
    all_tasks = tasks + comp_list
    task = input("Enter the task you want to mark as done: ").lower()
    if task.lower() in all_tasks:
        comp_list.append(task.lower())
        print("Task marked as done successfully.")
        all_tasks.remove(task)
        tasks.remove(task)
        counter = 1
        for item in comp_list:
            print(counter, item.capitalize())
            counter += 1
    else:
        print("Task does not found in the tasks list")
def completed():
    if len(comp_list) == 0:
        print("No completed tasks found.")
    else:
        counter = 1
        for item in comp_list:
            print(counter, item.capitalize())
            counter += 1
def pedding():
    all_tasks = tasks + comp_list
    if len(all_tasks) == 0:
        print("No pending tasks found.")
    else:
        counter = 1 
        for item in all_tasks:
            if item not in comp_list and item in all_tasks:
                print(counter, item.capitalize())
                counter += 1

# Main program loop
while True:
    show()
    choice = int(input("Enter your choice 1/2/3/4/5: "))
    if choice == 1:
        result = add_task()
        print(result)
    elif choice == 2:   
        view_tasks()
    elif choice == 3:
        message,task= delete_task()
        print(task.capitalize(),message)
    elif choice == 4:
        done()   
    elif choice == 5:
        print("Your completed tasks are: ")
        completed()
    elif choice == 6:
        pedding()
    elif choice == 7:
        print("Program terminated successfully..!")
        import sys
        exit()
    else:
        print("Wring choice. Please enter a valid choice.")