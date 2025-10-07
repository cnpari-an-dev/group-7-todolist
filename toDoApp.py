class Task:
    """
    Represents a single to-do task.

    Attributes:
        description (str): The text description of the task.
        completed (bool): Indicates whether the task is marked as done (default is False).
    """

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

    @staticmethod
    def add_task(tasks, description: str):
        """
        Add a new task to the given list.

        Args:
            tasks (list): The list containing Task objects.
            description (str): The task description provided by the user.
        """
        description = description.strip()
        if not description:
            print("Task description cannot be empty.")
            return

        new_task = Task(description)
        tasks.append(new_task)
        print(f"Task added: '{new_task}'")

    @staticmethod
    def remove_task(tasks, task_number):
        """
        Remove task/s from the to-do list by number.

        Args:
            tasks (list): The list containing Task objects.
            task_number (int): The task number (1-based index) to remove.
        """
        if 0 < task_number <= len(tasks):
            removed = tasks.pop(task_number - 1)
            print(f"Task '{removed}' has been removed.")
        else:
            print("Invalid task number.")

    @staticmethod
    def showTasks(tasks):
        """
        Display all tasks in the given list.

        Args:
            tasks (list): The list containing Task objects.
        """
        if not tasks:
            print("No tasks available.")
            return

        print("\nYour Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task.description}")

def main():
    tasks = []

    while True:
        print("\n===== TO-DO LIST MENU =====")
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Remove Task")
        print("4. Exit")
        print("===========================")

        choice = input("Enter choice (1-4): ").strip()

        if choice == "1":
            description = input("Enter task description: ")
            Task.add_task(tasks, description)

        elif choice == "2":
            Task.showTasks(tasks)

        elif choice == "3":
            if not tasks:
                print("No tasks to remove.")
                continue
            try:
                number = int(input("Enter task number to remove: "))
                Task.remove_task(tasks, number)
            except ValueError:
                print("Please enter a valid number.")

        elif choice == "4":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
