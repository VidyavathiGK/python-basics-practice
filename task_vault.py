class TaskVault:
    def __init__(self):
        self.tasks = []

    def add_task(self, task_name):
        self.tasks.append({"task": task_name, "completed": False})
        print(f"Added task: '{task_name}'")

    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]["completed"] = True
            print(f"Completed task: {self.tasks[index]['task']}")
        else:
            print("Invalid task index.")

    def show_tasks(self):
        print("\n--- Current Tasks ---")
        for i, t in enumerate(self.tasks):
            status = "[X]" if t["completed"] else "[ ]"
            print(f"{i}. {status} {t['task']}")

# Example usage:
if __name__ == "__main__":
    vault = TaskVault()
    vault.add_task("Review pull request")
    vault.add_task("Update documentation")
    vault.complete_task(0)
    vault.show_tasks()
