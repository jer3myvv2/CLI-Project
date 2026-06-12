class users:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name

    def _to_dict(self):
        return {
            'user_id': self.user_id,
            'name': self.name
        }


User = users
