import json
import os


class TaskService:
    def __init__(self, file_path='data/tasks.json'):
        self.file_path = file_path
        os.makedirs(os.path.dirname(file_path) or '.', exist_ok=True)

    def add_task(self, task):
        try:
            with open(self.file_path, 'r', encoding='utf-8') as f:
                tasks = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            tasks = []

        tasks.append(task._to_dict())

        with open(self.file_path, 'w', encoding='utf-8') as f:
            json.dump(tasks, f, indent=4)

        return task._to_dict()

    def update_task(self, task_id, title=None, project_id=None, user_id=None, completed=None):
        try:
            with open(self.file_path, 'r', encoding='utf-8') as f:
                tasks = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return False

        for task in tasks:
            if task['task_id'] == task_id:
                if title is not None:
                    task['title'] = title
                if project_id is not None:
                    task['project_id'] = project_id
                if user_id is not None:
                    task['user_id'] = user_id
                if completed is not None:
                    task['completed'] = completed
                with open(self.file_path, 'w', encoding='utf-8') as f:
                    json.dump(tasks, f, indent=4)
                return True
        return False

    def delete_task(self, task_id):
        try:
            with open(self.file_path, 'r', encoding='utf-8') as f:
                tasks = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return False

        updated_tasks = [task for task in tasks if task['task_id'] != task_id]
        if len(updated_tasks) == len(tasks):
            return False

        with open(self.file_path, 'w', encoding='utf-8') as f:
            json.dump(updated_tasks, f, indent=4)
        return True

    def add_task_to_project(self, project_id, task_data):
        """
        Reads projects.json, finds the project by ID, 
        adds the task, and saves the file.
        """
        with open(self.file_path, 'r+') as f:
            projects = json.load(f)
            for project in projects:
                if project['project_id'] == project_id:
                    project['tasks'].append(task_data)
                    f.seek(0)
                    json.dump(projects, f, indent=4)
                    f.truncate()
                    return True
        return False