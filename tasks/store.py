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

    def _get_or_raise(self, task_id):
        task = self.find(task_id)
        if task is None:
            raise KeyError(task_id)
        return task

    def _set_field(self, task_id, field, value):
        task = self._get_or_raise(task_id)
        task[field] = value
        return task

    def set_status(self, task_id, status):
        return self._set_field(task_id, "status", status)

    def set_due_date(self, task_id, due_date):
        _validate_due_date(due_date)
        return self._set_field(task_id, "due_date", due_date)

    def archive(self, task_id):
        return self._set_field(task_id, "archived", True)

    def add_tag(self, task_id, tag):
        task = self.find(task_id)
        task["tags"].append(tag)
        return task

    def find_by_tag(self, tag):
        return [task for task in self._tasks if tag in task["tags"]]

    def all(self):
        return list(self._tasks)