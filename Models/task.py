class Task:
    def __init__(self, task_id, title, project_id=None, user_id=None, completed=False):
        self.task_id = task_id
        self.title = title
        self.project_id = project_id
        self.user_id = user_id
        self.completed = completed

    def _to_dict(self):
        return {
            'task_id': self.task_id,
            'title': self.title,
            'project_id': self.project_id,
            'user_id': self.user_id,
            'completed': self.completed
        }