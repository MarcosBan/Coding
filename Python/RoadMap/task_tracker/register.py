import json
import os
from datetime import datetime

from task_status import TaskStatus


class Register:
    def __init__(self, filename="tasks.json"):
        self.filename = filename

    def create(self):
        if not os.path.exists(self.filename):
            with open(self.filename, "w") as file:
                json.dump([], file)

    def _load_tasks(self):
        self.create()
        with open(self.filename, "r") as file:
            return json.load(file)

    def _save_tasks(self, tasks):
        with open(self.filename, "w") as file:
            json.dump(tasks, file, indent=2)

    def _find_task(self, task_id):
        tasks = self._load_tasks()
        for task in tasks:
            if task.get("id") == task_id:
                return task
        return None

class TaskRegister(Register):
    def add_task(self, title, description, createdAt):
        tasks = self._load_tasks()
        new_task = {
            "id": len(tasks) + 1,
            "title": title or "",
            "description": description,
            "status": TaskStatus.TODO.value,
            "createdAt": createdAt,
            "updatedAt": None,
        }
        tasks.append(new_task)
        self._save_tasks(tasks)
        return new_task["id"]

    def get_tasks(self):
        return self._load_tasks()

    def get_tasks_filtered_by_status(self, status):
        tasks = self._load_tasks()
        return [task for task in tasks if task.get("status") == status]
    
    def mark_in_progress(self, task_id):
        return self._update_status(task_id, TaskStatus.IN_PROGRESS)

    def mark_done(self, task_id):
        return self._update_status(task_id, TaskStatus.DONE)

    def update_task(self, task_id, title, description):
        tasks = self._load_tasks()
        for task in tasks:
            if task.get("id") == task_id:
                task["title"] = title or task.get("title", "")
                task["description"] = description
                task["updatedAt"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                self._save_tasks(tasks)
                return f"Task {task_id} updated successfully."
        return f"Task with id {task_id} not found."

    def delete_task(self, task_id):
        tasks = self._load_tasks()
        filtered = [task for task in tasks if task.get("id") != task_id]
        if len(filtered) == len(tasks):
            return f"Task with id {task_id} not found."
        self._save_tasks(filtered)
        return f"Task {task_id} deleted successfully."

    def describe_task(self, task_id):
        return self._find_task(task_id)

    def _update_status(self, task_id, status):
        tasks = self._load_tasks()
        for task in tasks:
            if task.get("id") == task_id:
                task["status"] = status.value
                task["updatedAt"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                self._save_tasks(tasks)
                return f"Task {task_id} marked as {status.value}."
        return f"Task with id {task_id} not found."
