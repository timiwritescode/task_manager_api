from task_manager import api
from task_manager.routes import (TaskManager,
                                 TaskManagerList,
                                 NewUser) 

api.add_resource(TaskManager, '/api/tasks/<int:task_id>')   
api.add_resource(TaskManagerList, '/api/tasks')
api.add_resource(NewUser, '/api/register')
