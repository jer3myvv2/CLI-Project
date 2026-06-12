import unittest
import os
import json
from services.User_service import UserService
from Models.users import users

class TestUserService(unittest.TestCase):
    def setUp(self):
        self.test_file = 'data/test_users.json'
        with open(self.test_file, 'w') as f:
            json.dump([], f)
        self.service = UserService(self.test_file)

    def test_save_user(self):
        new_user = users("u1", "John Doe")
        self.service.save_user(new_user)
        with open(self.test_file, 'r') as f:
            data = json.load(f)
            self.assertEqual(len(data), 1)
            self.assertEqual(data[0]['name'], "John Doe")

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

if __name__ == '__main__':
    unittest.main()