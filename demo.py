"""Prints a short status report. Run with: python3 demo.py"""

from tasks.reports import completion_rate
from tasks.store import TaskStore


def main():
    store = TaskStore()

    store.add("Write the spec")
    store.add("Review the spec")
    store.add("Ship the feature")

    store.set_status(1, "done")

    tasks = store.all()
    done = [t for t in tasks if t["status"] == "done"]

    print("Tasks:     " + str(len(tasks)))
    print("Done:       " + str(len(done)))
    print("Completion: " + str(completion_rate(tasks)) + "%")


if __name__ == "__main__":
    main()