import os

tasks = []
tasks_size = len(tasks)

file_list = []


def read_dir():
    files = os.listdir(os.path.dirname(os.path.abspath(__file__)))
    exclude_files = [os.path.basename(__file__)]
    for item in files:
        if item not in exclude_files:
            file_list.append(item)


def print_dir():
    for item in file_list:
        print(item)


def create_file():
    print("Would you like to create a new file? (y/n):")
    choice = input()
    if choice == "y":
        new_file_name = input("Enter the name of the new file: ") + ".txt"
        loadfile = open(new_file_name, "a")
        read_dir()


def load_tasks():
    read_dir()
    if len(file_list) >= 1:
        print("")

    elif len(file_list) < 1:
        print("No files found.")
        create_file()

    print_dir()

    print("load file?:")
    choice = input()
    if choice == "y":
        print("what file?")
        choice = input()
        with open(choice, "r") as f:
            for word in f:
                # tasks.append(f.read())
                tasks.append(word)
    else:
        print("load cancelled")

    create_file()


def save_tasks():
    read_dir()
    print_dir()
    create_file()
    print("save file?:")
    choice = input()
    if choice == "y":
        print("what file?")
        choice = input()
        with open(choice, "w") as f:
            for task in tasks:
                f.write(task + "\n")
        with open(choice, "r") as f:
            print(f.read())
    else:
        print("save cancelled")


def view_tasks():
    if tasks_size == 0:
        print("you have no tasks")
    elif tasks_size == 1:
        print("you have 1 task")
    else:
        print("you have", tasks_size, "tasks")

    for i, x in enumerate(tasks, start=1):
        print(i, x)


def delete_task():
    view_tasks()
    print("What task would you like to remove?:")
    remove_task = int(input())
    tasks.pop(remove_task - 1)


def add_task():
    print("Whats your new task?:")
    new_task = input()
    tasks.append(new_task)


while True:
    print(
        "1. Add Task \n2. View Tasks \n3. Delete Task \n4. Save Tasks to File \n5. Load Tasks from File \nq. Quit \n"
    )
    menu_input = input()
    print("\n")
    if menu_input == "1":
        add_task()
        print("\n")
    elif menu_input == "2":
        view_tasks()
        print("\n")
    elif menu_input == "3":
        delete_task()
        print("\n")
    elif menu_input == "4":
        save_tasks()
        print("\n")
    elif menu_input == "5":
        load_tasks()
        print("\n")
    elif menu_input == "q":
        break
