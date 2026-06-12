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
        # Setup: Create a project and save it (manual add for test isolation)
        with open(self.test_file, 'w') as f:
            json.dump([{"project_id": "p1", "name": "Lab Test", "user_id": "u1", "tasks": []}], f)
        
        results = self.service.get_projects_by_user("u1")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]['name'], "Lab Test")

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

if __name__ == '__main__':
    unittest.main()