from flask import request
from flask_restful import Resource, reqparse, abort

from flask import Flask
from flask_restful import Api

app = Flask(__name__)
api = Api(app)

tasks = {1: {
    'title': "wash_cloth",
    'days': 1,
    'completed': False, 
}
}

taskmanager_put_args = reqparse.RequestParser()
taskmanager_put_args.add_argument("title", type=str, help="fetch all tasks", required=True)
taskmanager_put_args.add_argument("completed", type=bool, help="fetch all tasks", required=True)

# implement the methods class
class TaskManager(Resource):
    # list/view tasks
    def get(self, task_id):
        if task_id not in list(tasks.keys()):
            abort(409, message='Task does not exist')

        #args = taskmanager_get_args.parse_args() 
        if request.args.get('all') in ['true']:
            return tasks         

        result = tasks[task_id]
        print(result)
        return result, 200
    
    def put(self, task_id):
        if task_id in tasks:
            abort(409, message="ID already exist")

        args = taskmanager_put_args.parse_args()

        tasks[task_id] = args

        return tasks ,201    

api.add_resource(TaskManager, '/api/tasks/<int:task_id>')   


