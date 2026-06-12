import json
import os


class ProjectService:
    def __init__(self, file_path='data/projects.json'):
        self.file_path = file_path
        os.makedirs(os.path.dirname(file_path) or '.', exist_ok=True)

    def get_projects_by_user(self, user_id):
        """Filters projects by user_id from the JSON file."""
        if not os.path.exists(self.file_path):
            return []
        
        with open(self.file_path, 'r') as f:
            try:
                projects = json.load(f)
                return [p for p in projects if p['user_id'] == user_id]
            except json.JSONDecodeError:
                return []

    def save_project(self, project):
        """Persists a Project object to JSON."""
        try:
            with open(self.file_path, 'r', encoding='utf-8') as f:
                projects = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            projects = []

        projects.append(project._to_dict())

        with open(self.file_path, 'w', encoding='utf-8') as f:
            json.dump(projects, f, indent=4)

        return project._to_dict()