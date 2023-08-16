# this contains every util functions
from task_manager import db
from task_manager.models import TaskModel


def get_filtered_result(filter):
    """
    Function to get results from database according to filter
    """
    #tasks = db.session.execute(db.select(TaskModel).filter_by(completed=False)).scalars()
    tasks = TaskModel.query.filter_by(completed=filter).all()
    return tasks