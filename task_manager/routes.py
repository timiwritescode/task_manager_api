from task_manager import api
from task_manager.url_arguments import taskmanager_put_args, taskmanager_update_args
from flask import request
from flask_restful import Resource, abort 



TASKS = {1: {
    'title': "wash_cloth",
    'days': 1,
    'completed': False, 
}
}


# implement the methods class
# view, delete and put just one task 
class TaskManager(Resource):
    # list/view tasks
    def get(self, task_id):
        if task_id not in list(TASKS.keys()):
            abort(409, message='Task does not exist')

        result = TASKS[task_id]
        print(result)
        return result, 200
    
    def put(self, task_id):
        if task_id in TASKS:
            abort(409, message="ID already exist")

        args = taskmanager_put_args.parse_args()

        TASKS[task_id] = args

        return TASKS ,201  

    def patch(self, task_id):
        if task_id not in TASKS.keys():
            abort(404, 'no task with that ID')
        
        args = taskmanager_update_args.parse_args()
        if args['title']:
            TASKS[task_id]['title'] = args['title']

        if args['completed']:
            TASKS[task_id]['completed'] = args['completed']

        return TASKS ,200        

    def delete(self, task_id):
        if task_id not in TASKS.keys():
            abort(404, 'Id does not exist')

        del TASKS[task_id]
        return TASKS ,204          
    
# post multiple tasks     
class TaskManagerList(Resource):
    def get(self):
        return TASKS

    def post(self):
        task_id = len(TASKS.keys()) + 1
        args = taskmanager_put_args.parse_args()
        TASKS[task_id] = args
        return TASKS, 201

api.add_resource(TaskManager, '/api/tasks/<int:task_id>')   
api.add_resource(TaskManagerList, '/api/tasks')

