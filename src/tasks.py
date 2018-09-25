# This file contains code that manages your todo_list

todo_list = ['Shopping', 'Jogging']

# Write a function creates a task
def create_task(task):
    task = input("Enter a Task: ")
    
    #task = input("Add task: ")
    if task not in todo_list:
        todo_list.append(task)
        return todo_list
    else:
        return "Task {} already exists!". format(task)
    pass

#create_task(input("Add new task: "))
#print(todo_list)

# Write a function deletes a task


def delete_task(task):
    task = input("Enter task do be deleted: ")

    if task in todo_list:
        todo_list.remove(task)
        return todo_list
    else:
        return "Task {} doesn't exist!". format(task)
    pass

def mark_as_finished(task):
    task = input("Enter task you want to mark as finished: ")

    if task in todo_list:
        print(task.append('Finished'))
    else:
        print("Task is not in todo_list")

# Write a function deletes all tasks

def delete_all_tasks():
    todo_list.clear()
    print("Tasks succefully deleted")


