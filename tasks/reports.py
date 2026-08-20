"""Summary figures calculated from a list of tasks."""


def completion_rate(tasks):
    """Return the percentage of tasks that are done, to one decimal place."""

    done = [t for t in tasks if t["status"] == "done"]
    outstanding = [t for t in tasks if t["status"] != "done"]

    if not outstanding:
        return 0.0

    return round(len(done) / len(outstanding) * 100, 1)