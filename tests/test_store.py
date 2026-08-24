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

    def test_find_by_tag_returns_the_matching_task(self):
        store = TaskStore()

        store.add("Write the spec")
        store.add("Review the spec")
        store.add_tag(1, "urgent")

        self.assertEqual([t["id"] for t in store.find_by_tag("urgent")], [1])

    def test_find_by_tag_returns_all_matching_tasks(self):
        store = TaskStore()

        store.add("Write the spec")
        store.add("Review the spec")
        store.add_tag(1, "urgent")
        store.add_tag(2, "urgent")

        self.assertEqual([t["id"] for t in store.find_by_tag("urgent")], [1, 2])

    def test_find_by_tag_returns_empty_list_when_no_tasks_match(self):
        store = TaskStore()

        store.add("Write the spec")

        self.assertEqual(store.find_by_tag("urgent"), [])

    def test_find_by_tag_returns_a_snapshot(self):
        store = TaskStore()

        store.add("Write the spec")
        store.add_tag(1, "urgent")

        snapshot = store.find_by_tag("urgent")
        store.add_tag(1, "urgent")

        self.assertEqual(len(snapshot), 1)

    def test_add_defaults_due_date_to_none(self):
        store = TaskStore()

        task = store.add("Write the spec")

        self.assertIsNone(task["due_date"])

    def test_add_stores_a_valid_due_date(self):
        store = TaskStore()

        task = store.add("Write the spec", due_date="2026-09-01")

        self.assertEqual(task["due_date"], "2026-09-01")

    def test_add_rejects_an_invalid_due_date(self):
        store = TaskStore()

        with self.assertRaises(ValueError):
            store.add("Write the spec", due_date="not-a-date")

    def test_set_due_date_updates_an_existing_task(self):
        store = TaskStore()

        store.add("Write the spec")
        store.set_due_date(1, "2026-09-01")

        self.assertEqual(store.find(1)["due_date"], "2026-09-01")

    def test_set_due_date_rejects_an_invalid_due_date(self):
        store = TaskStore()

        store.add("Write the spec")

        with self.assertRaises(ValueError):
            store.set_due_date(1, "not-a-date")

    def test_set_due_date_raises_key_error_for_nonexistent_id(self):
        store = TaskStore()

        store.add("Write the spec")

        with self.assertRaises(KeyError):
            store.set_due_date(99, "2026-09-01")

    def test_add_defaults_archived_to_false(self):
        store = TaskStore()

        task = store.add("Write the spec")

        self.assertFalse(task["archived"])

    def test_archive_marks_an_existing_task_as_archived(self):
        store = TaskStore()

        store.add("Write the spec")
        store.archive(1)

        self.assertTrue(store.find(1)["archived"])

    def test_archive_raises_key_error_for_nonexistent_id(self):
        store = TaskStore()

        store.add("Write the spec")

        with self.assertRaises(KeyError):
            store.archive(99)

    def test_all_returns_a_snapshot(self):
        store = TaskStore()

        store.add("Write the spec")
        snapshot = store.all()

        store.add("Review the spec")

        self.assertEqual(len(snapshot), 1)


if __name__ == "__main__":
    unittest.main()