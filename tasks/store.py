"""In-memory storage for tasks."""

VALID_STATUSES = ("pending", "in_progress", "done")


class TaskStore:
    """Holds tasks in memory and hands out sequential ids."""

    def __init__(self):
        self._tasks = []
        self._next_id = 1

    def add(self, title, status="pending", tags=None):
        if tags is None:
            tags = []

        task = {
            "id": self._next_id,
            "title": title,
            "status": status,
            "tags": tags,
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

    def add_tag(self, task_id, tag):
        task = self.find(task_id)
        task["tags"].append(tag)
        return task

    def all(self):
        return list(self._tasks)