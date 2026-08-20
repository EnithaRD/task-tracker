import unittest

from tasks.store import TaskStore


class TestTaskStore(unittest.TestCase):

    def test_add_assigns_sequential_ids(self):
        store = TaskStore()

        first = store.add("Write the spec")
        second = store.add("Review the spec")

        self.assertEqual(first["id"], 1)
        self.assertEqual(second["id"], 2)

    def test_find_returns_the_matching_task(self):
        store = TaskStore()

        store.add("Write the spec")
        found = store.find(1)

        self.assertEqual(found["title"], "Write the spec")

    def test_set_status_updates_an_existing_task(self):
        store = TaskStore()

        store.add("Write the spec")
        store.set_status(1, "done")

        self.assertEqual(store.find(1)["status"], "done")

    def test_set_status_rejects_an_unknown_id(self):
        store = TaskStore()

        store.add("Write the spec")

        with self.assertRaises(KeyError):
            store.set_status(99, "done")

    def test_tags_are_not_shared_between_tasks(self):
        store = TaskStore()

        store.add("Write the spec")
        store.add("Review the spec")

        store.add_tag(1, "urgent")

        self.assertEqual(store.find(2)["tags"], [])

    def test_set_status_raises_key_error_for_nonexistent_id(self):
        store = TaskStore()

        store.add("Write the spec")
        store.add("Review the spec")

        with self.assertRaises(KeyError):
            store.set_status(42, "done")

    def test_add_gives_each_task_its_own_tags_list(self):
        store = TaskStore()

        first = store.add("Write the spec")
        second = store.add("Review the spec")

        self.assertIsNot(first["tags"], second["tags"])

        first["tags"].append("urgent")

        self.assertEqual(second["tags"], [])

    def test_all_returns_a_snapshot(self):
        store = TaskStore()

        store.add("Write the spec")
        snapshot = store.all()

        store.add("Review the spec")

        self.assertEqual(len(snapshot), 1)


if __name__ == "__main__":
    unittest.main()