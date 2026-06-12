import json
import os


class UserService:
    def __init__(self, file_path='data/users.json'):
        self.file_path = file_path
        os.makedirs(os.path.dirname(file_path) or '.', exist_ok=True)
        self.users = self._load_users()

    def _load_users(self):
        try:
            with open(self.file_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_user(self, user):
        users = self._load_users()
        users.append(user._to_dict())
        with open(self.file_path, 'w', encoding='utf-8') as f:
            json.dump(users, f, indent=4)
        self.users = users

    def save_users(self, user):
        self.save_user(user)