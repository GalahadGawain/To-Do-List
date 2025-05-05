import json
import os

file_name = "todo_list.json"


def display_program_name():
    os.system("cls")
    print("\n To-Do List Manager")
    print("=" * 20)


def display_menu_options():
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Exit")


def end_app():
    print("Goodbye\n")
    print("Closing the program...")


def return_to_main_menu():
    input("\nPress Enter to return to the main menu...\n")
    main()


def invalid_option():
    print("Invalid option. Try again.\n")
    return_to_main_menu()


def load_tasks():
    try:
        with open(file_name, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {"tasks": []}
    except json.JSONDecodeError:
        print("Error decoding JSON from file. Starting with an empty task list.")
        return {"tasks": []}


def save_tasks(tasks):
    try:
        with open(file_name, "w") as file:
            json.dump(tasks, file, indent=4)
    except IOError:
        print("Failed to save tasks to file.")


def view_tasks(tasks):
    tasks_list = tasks["tasks"]
    if not tasks_list:
        print("No tasks to display.")
    else:
        print("\nYour To Do List: \n")
        for index, task in enumerate(tasks_list):
            status = "[Completed]" if task["complete"] else "[Pending]"
            print(f"{index + 1}. {task['description']} | {status}")


def create_task(tasks):
    description = input("Enter the task Description: ").strip()
    if description:
        tasks["tasks"].append({"description": description, "complete": False})
        save_tasks(tasks)
        print("\nTask added successfully.")
    else:
        print("\nTask description cannot be empty.")


def mark_task_complete(tasks):
    view_tasks(tasks)
    if tasks["tasks"]:
        try:
            task_number = int(
                input("Enter the task number to mark as complete: ").strip()
            )
            if 1 <= task_number <= len(tasks["tasks"]):
                tasks["tasks"][task_number - 1]["complete"] = True
                save_tasks(tasks)
                print("\nTask marked as complete.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    else:
        print("No tasks available to mark as complete.")


def delete_task(tasks):
    view_tasks(tasks)
    if tasks["tasks"]:
        try:
            task_number = int(input("Enter the task number to delete: ").strip())
            if 1 <= task_number <= len(tasks["tasks"]):
                deleted_task = tasks["tasks"].pop(task_number - 1)
                save_tasks(tasks)
                print(f"\nTask '{deleted_task['description']}' deleted successfully.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    else:
        print("No tasks available to delete.")


def choose_option(tasks):
    try:
        choice = int(input("\nEnter Menu Choice: ").strip())

        if choice == 1:
            view_tasks(tasks)
            return_to_main_menu()
        elif choice == 2:
            create_task(tasks)
            return_to_main_menu()
        elif choice == 3:
            mark_task_complete(tasks)
            return_to_main_menu()
        elif choice == 4:
            delete_task(tasks)
            return_to_main_menu()
        elif choice == 5:
            end_app()
        else:
            invalid_option()
    except:
        invalid_option()


def main():
    tasks = load_tasks()

    os.system("cls")
    display_program_name()
    display_menu_options()
    choose_option(tasks)


if __name__ == "__main__":
    main()
