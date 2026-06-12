class Project:
    def __init__(self, project_id, name, description, user_id):
        self.project_id = project_id
        self.name = name
        self.description = description
        self.user_id = user_id
        self.tasks = []  # List to hold tasks associated with the project
    def add_task(self, task):
        self.tasks.append(task)
    def _to_dict(self):
        return {
            'project_id': self.project_id,
            'name': self.name,
            'description': self.description,
            'user_id': self.user_id,
            'tasks': [task._to_dict() for task in self.tasks]  # Convert tasks to dicts
        }