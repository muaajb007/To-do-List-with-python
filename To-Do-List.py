class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})

    def mark_task_completed(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index]["completed"] = True
        else:
            print("Invalid task index")

    def delete_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            del self.tasks[task_index]
        else:
            print("Invalid task index")

    def display_tasks(self):
        print("To-Do List:")
        for i, task in enumerate(self.tasks):
            status = "✓" if task["completed"] else "✗"
            print(f"{i + 1}. [{status}] {task['task']}")


def main():
    todo_list = TodoList()
    while True:
        print("\nWhat would you like to do?")
        print("1. Add a task")
        print("2. Mark a task as completed")
        print("3. Delete a task")
        print("4. View tasks")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter task: ")
            todo_list.add_task(task)
            print("Task added successfully!")
        elif choice == "2":
            task_index = int(input("Enter task number to mark as completed: ")) - 1
            todo_list.mark_task_completed(task_index)
            print("Task marked as completed!")
        elif choice == "3":
            task_index = int(input("Enter task number to delete: ")) - 1
            todo_list.delete_task(task_index)
            print("Task deleted successfully!")
        elif choice == "4":
            todo_list.display_tasks()
        elif choice == "5":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
