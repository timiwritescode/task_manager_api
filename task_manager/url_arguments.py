from flask_restful import reqparse

taskmanager_put_args = reqparse.RequestParser()
taskmanager_put_args.add_argument("title", type=str, help="title of task required", required=True)
taskmanager_put_args.add_argument("completed", type=bool, help="task status required", required=True)
taskmanager_put_args.add_argument("description", type=str, help="description of task")
taskmanager_put_args.add_argument("priority", type=int, help="the priority of task")

taskmanager_update_args = reqparse.RequestParser()
taskmanager_update_args.add_argument('title', type=str, help='title of task required')
taskmanager_update_args.add_argument('completed',type=bool, help='task status required')
taskmanager_update_args.add_argument("description", type=str, help="description of task")

taskmanager_get_args = reqparse.RequestParser()
taskmanager_get_args.add_argument("filter_by_completed", type=bool, help='true or false')
taskmanager_get_args.add_argument("order_by_priority", type=bool, help="true or false")