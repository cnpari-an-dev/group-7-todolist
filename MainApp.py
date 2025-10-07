class MainApp:
    """
    Main application that provides a console interface for the To-Do List.

    This class manages the main program loop, displays the menu,
    and interacts with the TaskManager to perform operations such as
    adding, showing, and removing tasks.
    """

    def __init__(self):
        """
        Initialize the MainApp with a TaskManager instance.
        """
        self.manager = TaskManager()

    def run(self):
        """
        Run the main loop of the application.

        Displays a text-based menu with options to:
            1. Add a task
            2. Show all tasks
            3. Remove a task
            4. Exit the application

        Handles user input, validates choices, and calls
        TaskManager methods to perform the requested actions.
        """
        while True:
            print("\n--- To-Do List Menu ---")
            print("1. Add Task")
            print("2. Show Tasks")
            print("3. Remove Task")
            print("4. Exit")

            choice = input("Enter choice: ").strip()

            if choice == "1":
                task = input("Enter task: ")
                self.manager.add_task(task)
            elif choice == "2":
                self.manager.show_tasks()
            elif choice == "3":
                try:
                    number = int(input("Enter task number to remove: "))
                    self.manager.remove_task(number)
                except ValueError:
                    print("Please enter a valid number.")
            elif choice == "4":
                print("Exiting... Thank you for using this program!")
                break
            else:
                print("Invalid choice. Please try again.")
