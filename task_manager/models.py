from task_manager import db

class TaskModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable = False)
    completed = db.Column(db.Boolean, nullable =False) 
    description = db.Column(db.String)


    


