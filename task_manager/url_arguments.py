from flask_restful import reqparse

taskmanager_put_args = reqparse.RequestParser()
taskmanager_put_args.add_argument("title", type=str, help="title of task required", required=True)
taskmanager_put_args.add_argument("completed", type=bool, help="task status required", required=True)

taskmanager_update_args = reqparse.RequestParser()
taskmanager_update_args.add_argument('title', type=str, help='title of task required')
taskmanager_update_args.add_argument('completed',type=bool, help='task status required')