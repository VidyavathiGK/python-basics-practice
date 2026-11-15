import sqlite3

class SQLiteTodoManager:
    def __init__(self, db_name: str = "tasks.db"):
        self.conn = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self) -> None:
        with self.conn:
            self.conn.execute("""
                CREATE TABLE IF NOT EXISTS tasks (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    completed BOOLEAN NOT NULL DEFAULT 0
                )
            """)

    def add_task(self, title: str) -> None:
        with self.conn:
            self.conn.execute("INSERT INTO tasks (title) VALUES (?)", (title,))
        print(f"Added task: '{title}'")

    def list_tasks(self) -> None:
        cursor = self.conn.execute("SELECT id, title, completed FROM tasks")
        rows = cursor.fetchall()
        if not rows:
            print("No tasks found.")
            return
        print("\n--- To-Do List ---")
        for task_id, title, completed in rows:
            status = "✓" if completed else " "
            print(f"[{status}] {task_id}: {title}")

    def complete_task(self, task_id: int) -> None:
        with self.conn:
            self.conn.execute("UPDATE tasks SET completed = 1 WHERE id = ?", (task_id,))
        print(f"Marked task #{task_id} as completed.")

if __name__ == "__main__":
    todo = SQLiteTodoManager()
    todo.add_task("Review pull requests")
    todo.add_task("Refactor data cleaner script")
    todo.list_tasks()
    todo.complete_task(1)
    todo.list_tasks()
