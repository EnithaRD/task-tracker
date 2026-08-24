"""In-memory storage for tasks."""

from datetime import date

VALID_STATUSES = ("pending", "in_progress", "done")


def _validate_due_date(due_date):
    if due_date is None:
        return

    try:
        date.fromisoformat(due_date)
    except (TypeError, ValueError):
        raise ValueError(
            "due_date must be an ISO date string (YYYY-MM-DD) or None"
        )


class TaskStore:
    """Holds tasks in memory and hands out sequential ids."""

    def __init__(self):
        self._tasks = []
        self._next_id = 1

    def add(self, title, status="pending", tags=None, due_date=None):
        if tags is None:
            tags = []

        _validate_due_date(due_date)

        task = {
            "id": self._next_id,
            "title": title,
            "status": status,
            "tags": tags,
            "due_date": due_date,
            "archived": False,
        }

        self._tasks.append(task)
        self._next_id += 1
        return task

    def find(self, task_id):
        for task in self._tasks:
            if task["id"] == task_id:
                return task
        return None

    def set_status(self, task_id, status):
        task = self.find(task_id)
        if task is None:
            raise KeyError(task_id)
        task["status"] = status
        return task

    def set_due_date(self, task_id, due_date):
        task = self.find(task_id)
        if task is None:
            raise KeyError(task_id)
        _validate_due_date(due_date)
        task["due_date"] = due_date
        return task

    def archive(self, task_id):
        task = self.find(task_id)
        if task is None:
            raise KeyError(task_id)
        task["archived"] = True
        return task

    def add_tag(self, task_id, tag):
        task = self.find(task_id)
        task["tags"].append(tag)
        return task

    def find_by_tag(self, tag):
        return [task for task in self._tasks if tag in task["tags"]]

    def all(self):
        return list(self._tasks)