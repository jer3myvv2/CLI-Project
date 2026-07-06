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

    def get_all_users(self):
        return self._load_users()

    def save_user(self, user):
        users = self._load_users()
        users.append(user._to_dict())
        with open(self.file_path, 'w', encoding='utf-8') as f:
            json.dump(users, f, indent=4)
        self.users = users

    def update_user(self, user_id, name=None):
        users = self._load_users()
        for user in users:
            if not isinstance(user, dict) or user.get('user_id') != user_id:
                continue
            if name is not None:
                user['name'] = name
            with open(self.file_path, 'w', encoding='utf-8') as f:
                json.dump(users, f, indent=4)
            self.users = users
            return True
        return False

    def delete_user(self, user_id):
        users = self._load_users()
        updated_users = [user for user in users if isinstance(user, dict) and user.get('user_id') != user_id]
        if len(updated_users) == len(users):
            return False
        with open(self.file_path, 'w', encoding='utf-8') as f:
            json.dump(updated_users, f, indent=4)
        self.users = updated_users
        return True

    def save_users(self, user):
        self.save_user(user)