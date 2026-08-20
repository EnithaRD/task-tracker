"""Summary figures calculated from a list of tasks."""


def completion_rate(tasks):
    """Return the percentage of tasks that are done, to one decimal place."""

    if not tasks:
        return 0.0

    done = [t for t in tasks if t["status"] == "done"]

    return round(len(done) / len(tasks) * 100, 1)