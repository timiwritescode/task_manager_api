from flask_restful import reqparse

newuser_post_args = reqparse.RequestParser()
newuser_post_args.add_argument('username', type=str, help="username required", required=True)
newuser_post_args.add_argument('email', type=str, help="email required", required=True)

taskmanager_post_args = reqparse.RequestParser()
taskmanager_post_args.add_argument("title", type=str, help="title of task required", required=True)
taskmanager_post_args.add_argument("completed", type=bool, help="task status required", required=True)
taskmanager_post_args.add_argument("description", type=str, help="description of task")
taskmanager_post_args.add_argument("priority", type=int, help="the priority of task")
taskmanager_post_args.add_argument("due_at", type=str, help="the priority of task", required=True)


taskmanager_update_args = reqparse.RequestParser()
taskmanager_update_args.add_argument('title', type=str, help='title of task required')
taskmanager_update_args.add_argument('completed',type=bool, help='task status required')
taskmanager_update_args.add_argument("description", type=str, help="description of task")

taskmanager_get_args = reqparse.RequestParser()
taskmanager_get_args.add_argument("filter_by_completed", type=bool, help='true or false')
taskmanager_get_args.add_argument("order_by_priority", type=bool, help="true or false")
taskmanager_get_args.add_argument("page_number", type=int, help='page number was not given', required=True)
taskmanager_get_args.add_argument("items_per_page", type=int, help="number of items per page")