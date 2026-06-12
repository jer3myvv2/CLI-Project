import unittest
import os
import json
from services.task_service import TaskService
from Models.task import Task

class TestTaskService(unittest.TestCase):
    def setUp(self):
        self.test_file = 'data/test_tasks.json'
        with open(self.test_file, 'w') as f:
            json.dump([], f)
        self.service = TaskService(self.test_file)

    def test_add_task(self):
        new_task = Task("t1", "Complete Lab", "p1", "u1")
        self.service.add_task(new_task)

        with open(self.test_file, 'r') as f:
            data = json.load(f)
            self.assertEqual(len(data), 1)
            self.assertEqual(data[0]['title'], "Complete Lab")

    def test_update_and_delete_task(self):
        self.service.add_task(Task("t1", "Complete Lab", "p1", "u1", False))

        updated = self.service.update_task("t1", title="Done Lab", completed=True)
        self.assertTrue(updated)

        with open(self.test_file, 'r') as f:
            data = json.load(f)
            self.assertEqual(data[0]['title'], "Done Lab")
            self.assertTrue(data[0]['completed'])

        deleted = self.service.delete_task("t1")
        self.assertTrue(deleted)

        with open(self.test_file, 'r') as f:
            self.assertEqual(json.load(f), [])

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

if __name__ == '__main__':
    unittest.main()