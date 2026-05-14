from datetime import datetime

from register import TaskRegister
from formatter import format_tasks


class TaskTracker:
    """High-level task management service."""

    def __init__(self, repository=None, formatter=None):
        """
        Initialize TaskTracker with optional dependencies.
        If not provided, defaults are used.
        """
        self.repository = repository or TaskRegister()
        self.formatter = formatter or format_tasks
    def create_task(self, title, description):
        register_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        task_id = self.repository.add_task(title, description, register_date)
        return f"Task created successfully with id: {task_id}"

    def list_tasks(self):
        return self.repository.get_tasks()

    def list_tasks_status(self, status):
        return self.repository.get_tasks_filtered_by_status(status)

    def mark_task_in_progress(self, task_id):
        return self.repository.mark_in_progress(task_id)

    def mark_task_done(self, task_id):
        return self.repository.mark_done(task_id)

    def update_task(self, task_id, title, description):
        return self.repository.update_task(task_id, title, description)

    def delete_task(self, task_id):
        return self.repository.delete_task(task_id)

    def describe_task(self, task_id):
        return self.repository.describe_task(task_id)

    def format_tasks(self, tasks):
        """Format tasks using the injected formatter function."""
        return self.formatter(tasks)
