from task_manager import api, db
from task_manager.models import TaskModel
from task_manager.util.util import get_filtered_result, match_priority_with_order
from task_manager.url_arguments import (taskmanager_put_args, 
taskmanager_update_args, 
taskmanager_get_args)
from flask_restful import Resource, abort, fields, marshal_with 
from flask import jsonify

resource_fields = {
    "id": fields.Integer,
    "title": fields.String,
    "completed": fields.Boolean,
    "description": fields.String,
    "priority": fields.String,
    "order": fields.Integer
}
 
class TaskManager(Resource):
    @marshal_with(resource_fields)
    def get(self, task_id):
        task = db.get_or_404(TaskModel, task_id, description='Id does not exist')
        return task, 200
    

    @marshal_with(resource_fields)
    def patch(self, task_id):   
        args = taskmanager_update_args.parse_args()
        result = db.get_or_404(TaskModel, task_id, description='Id does not exist')
        result.title = args['title'] if args['title'] else TaskModel.title
        result.description = args['description'] if args['description'] else TaskModel.description
        result.completed = args['completed'] if args['completed'] else TaskModel.completed
        db.session.add(result)
        db.session.commit()    
        
        return 200        

    
    def delete(self, task_id):
        task = db.get_or_404(TaskModel, task_id, description='Id does not exist')
        
        db.session.delete(task)
        db.session.commit()
        return 204           
         
class TaskManagerList(Resource):
    @marshal_with(resource_fields)
    def get(self):
        request_arguments = taskmanager_get_args.parse_args()
        page_number = request_arguments['page_number']
        items_per_page = 20 if not request_arguments["items_per_page"] else request_arguments["items_per_page"]
        
        page = db.paginate(db.select(TaskModel), per_page=items_per_page, page=page_number)
        if request_arguments['order_by_priority']:
            page = db.paginate(db.select(TaskModel).order_by(TaskModel.order), per_page=items_per_page, page=page_number)

            
        page_data = [{'id': item.id, 
                         'title': item.title, 
                         'completed': item.completed, 
                         'description':item.description,
                         'priority': item.priority,
                         'order':item.order} for item in page] 
        
        filter_result = request_arguments['filter_by_completed'] 
        
        if filter_result is not None:
            return get_filtered_result(filter_result)
         
        return page_data
    
    def post(self):
        tasks = db.session.execute(db.select(TaskModel)).scalars()
        # tasks returns a generator with the 'select' db query 
        results_data = [task for task in tasks]
        new_task_id = len(results_data) 
        request_arguments = taskmanager_put_args.parse_args() 
        new_task = TaskModel(id=new_task_id, 
                             title=request_arguments['title'].lower(),
                             completed=request_arguments['completed'],
                             description=request_arguments['description'],
                             priority=match_priority_with_order(request_arguments['priority']),
                             order=request_arguments['priority']
                             ) 
        
        db.session.add(new_task)
        db.session.commit()
        return "Successfully created new task", 201


api.add_resource(TaskManager, '/api/tasks/<int:task_id>')   
api.add_resource(TaskManagerList, '/api/tasks')

