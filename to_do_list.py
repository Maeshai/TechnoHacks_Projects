class ToDoList:
        def __init__(self):
                    self.tasks = []

                        def add_task(self, task):
                                    self.tasks.append(task)
                                            print(f"Task added: {task}")

                                                def view_tasks(self):
                                                            if self.tasks:
                                                                            print("Your To-Do List:")
                                                                                        for i, task in enumerate(self.tasks, 1):
                                                                                                            print(f"{i}. {task}")
                                                                                                                    else:
                                                                                                                                    print("Your To-Do List is empty.")

                                                                                                                                        def remove_task(self, task_number):
                                                                                                                                                    if 0 < task_number <= len(self.tasks):
                                                                                                                                                                    removed_task = self.tasks.pop(task_number - 1)
                                                                                                                                                                                print(f"Task removed: {removed_task}")
                                                                                                                                                                                        else:
                                                                                                                                                                                                        print("Invalid task number.")

                                                                                                                                                                                                        def main():
                                                                                                                                                                                                                todo_list = ToDoList()
                                                                                                                                                                                                                    while True:
                                                                                                                                                                                                                                print("\nTo-Do List Manager")
                                                                                                                                                                                                                                        print("1. Add a task")
                                                                                                                                                                                                                                                print("2. View tasks")
                                                                                                                                                                                                                                                        print("3. Remove a task")
                                                                                                                                                                                                                                                                print("4. Exit")
                                                                                                                                                                                                                                                                        choice = input("Enter your choice: ")

                                                                                                                                                                                                                                                                                if choice == '1':
                                                                                                                                                                                                                                                                                                task = input("Enter the task: ")
                                                                                                                                                                                                                                                                                                            todo_list.add_task(task)
                                                                                                                                                                                                                                                                                                                    elif choice == '2':
                                                                                                                                                                                                                                                                                                                                    todo_list.view_tasks()
                                                                                                                                                                                                                                                                                                                                            elif choice == '3':
                                                                                                                                                                                                                                                                                                                                                            task_number = int(input("Enter the task number to remove: "))
                                                                                                                                                                                                                                                                                                                                                                        todo_list.remove_task(task_number)
                                                                                                                                                                                                                                                                                                                                                                                elif choice == '4':
                                                                                                                                                                                                                                                                                                                                                                                                break
                                                                                                                                                                                                                                                                                                                                                                                                    else:
                                                                                                                                                                                                                                                                                                                                                                                                                    print("Invalid choice. Please try again.")

                                                                                                                                                                                                                                                                                                                                                                                                                    if __name__ == "__main__":
                                                                                                                                                                                                                                                                                                                                                                                                                            main()

