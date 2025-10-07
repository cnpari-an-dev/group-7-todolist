# toDoApp.py

def remove_task(self, task_number):
    """
    Remove task/s from the to-do list by number.

    Args:
        task_number: Remove task number by 1 index.
    """

    if 0 < task_number <= len(self.tasks):
        self.tasks.pop(task_number - 1)
        print("Task has been removed.")
    else:
        print("Invalid task number.")