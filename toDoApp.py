# toDoApp.py

class Task:

    """
        Represents a single to-do task.

        Attributes:
            description (str): The text description of the task.
            completed (bool): Indicates whether the task is marked as done (default is False).
    """


   def __init__(self, description: str):
        self.description = description.strip()

    def __str__(self):
        return self.description

        """
            Fixed a few indentations to improve readability for further modification
            
        """
def addtask(task):
    tasks.append(task)
    print("task added!")


def showTasks():
    if len(tasks) == 0:
        print("no tasks yet")
    else:
        for i in range(len(tasks)):
            print(i+1, ".", tasks[i])


def removetask(tasknumber):
    tasks.pop(tasknumber)
    print("task removed!!")


def main():
    while True:
        print("1 Add Task")
        print("2.Show Tasks")
        print("3.Remove Task")
        print("4- Exit")
        ch = input("enter choice : ")
        if ch == "1":
            t = input("enter task : ")
            addtask(t)
        elif ch == "2":
            showTasks()
        elif ch == "3":
            n = int(input("enter task no to remove: "))
            removetask(n)
        elif ch == "4":
            break
        else:
            print("wrong choice!!")


main()
