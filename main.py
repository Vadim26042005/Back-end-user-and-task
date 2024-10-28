class User:
    def __init__(self, name, id):
        self.name=name
        self.id=id

class Task:
    def __init__(self, name, created_date, id, duration, user_id, ):
        self.name = name
        self.created_date = created_date
        self.id = id
        self.duration = duration
        self.user_object = user_id
