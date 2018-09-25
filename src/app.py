
# This file contains the entry point to your tasks
# and the logic to manage it

from tasks import *
from accounts import *

name = input("Enter user name: ")
password = input("Enter password: ")


#if name == accounts['name'] and password == accounts['password']:
if __name__ == "__main__":
        print("Select Option:")
        print("1: Create Task")
        print("2: Delete Task")
        print("3: Mark All Tasks as Finished")
        print("4: Delete all tasks")

        selection = input("selection: ")
if selection == "1":
        task = input("Enter your task here: ")
elif selection == "2":
        delete_task(input("Remove Task: "))
        print(f"These are the items in your to_do list: {todo_list}")
elif selection == "3":
        mark_as_finished(input("Finished Task: "))
        print(todo_list)
elif selection == "4":
        delete_all_tasks()
        print("All tasks have been deleted")
        print(f"These are the items in your to_do list: {todo_list}")
else:
        print("Selection is invalid try again!")


                


