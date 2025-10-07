class TaskManager:
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
