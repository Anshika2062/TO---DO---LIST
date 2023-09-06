# Initializing an empty list to store tasks
tasks = []

# function to add tasks in the to-do list
def add(task):
    tasks.append(task)
    print(f"{task} added to the list")

# function to remove tasks from the to-do list
def remove(task):
    if task in tasks:
        tasks.remove(task)
        print(f"{task} is removed from the list")

    else:
        print(f"{task} is invalid entry. Please enter the valid task.")

# function to view the to-do list
def view():

    print("TO - DO - LIST\n")

    for i in range(len(tasks)):
            print(f"{i + 1}. {tasks[i]}")



#user input loop

while True:
    
    #choices given to the user

    print("\nOptions:")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. Show Tasks")
       

    choice = input("Enter your choice: ")
    
    if choice == "1":
        task = input("Enter the task to add: ")
        add(task)
    elif choice == "2":
        task = input("Enter the task to remove: ")
        remove(task)
    elif choice == "3":
        view()

        
    else:
        print("Invalid choice. Please try again.")
