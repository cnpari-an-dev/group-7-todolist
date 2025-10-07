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
