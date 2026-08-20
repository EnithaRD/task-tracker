import unittest

from tasks.reports import completion_rate


class TestCompletionRate(unittest.TestCase):

    def test_all_tasks_done(self):
        tasks = [
            {"status": "done"},
            {"status": "done"},
            {"status": "done"},
        ]

        self.assertEqual(completion_rate(tasks), 100.0)

    def test_mixed_done_and_pending(self):
        tasks = [
            {"status": "done"},
            {"status": "done"},
            {"status": "done"},
            {"status": "pending"},
        ]

        self.assertEqual(completion_rate(tasks), 75.0)

    def test_empty_task_list(self):
        self.assertEqual(completion_rate([]), 0.0)


if __name__ == "__main__":
    unittest.main()
