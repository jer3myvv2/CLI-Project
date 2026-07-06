import unittest
import os
import json
from services.Project_service import ProjectService
from Models.Project import Project

class TestProjectService(unittest.TestCase):
    def setUp(self):
        self.test_file = 'data/test_projects.json'
        with open(self.test_file, 'w') as f:
            json.dump([], f)
        self.service = ProjectService(self.test_file)

    def test_get_projects_by_user(self):
        with open(self.test_file, 'w') as f:
            json.dump([{"project_id": "p1", "name": "Lab Test", "user_id": "u1", "tasks": []}], f)

        results = self.service.get_projects_by_user("u1")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]['name'], "Lab Test")

    def test_update_and_delete_project(self):
        self.service.save_project(Project("p1", "Lab Test", "Initial", "u1"))

        updated = self.service.update_project("p1", name="Updated Lab", description="Updated")
        self.assertTrue(updated)

        with open(self.test_file, 'r') as f:
            data = json.load(f)
            self.assertEqual(data[0]['name'], "Updated Lab")
            self.assertEqual(data[0]['description'], "Updated")

        deleted = self.service.delete_project("p1")
        self.assertTrue(deleted)

        with open(self.test_file, 'r') as f:
            self.assertEqual(json.load(f), [])

    def test_update_delete_project_handles_malformed_records(self):
        with open(self.test_file, 'w') as f:
            json.dump([{"name": "Broken"}], f)

        self.assertFalse(self.service.update_project("p1", name="Safe"))
        self.assertFalse(self.service.delete_project("p1"))

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

if __name__ == '__main__':
    unittest.main()