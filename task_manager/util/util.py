# this contains every util functions

class Task:
    def __init__(self, id):
        self.id = id
        

class TaskManager(Task):
    def get_completed_tasks(self, id):
        """
        Function to list all tasks that have been completed
        """   
        if id in self.tasks.keys():
            pass 

    def get_number_of_tasks(self, id):
        """
        Function to get the total number of tasks currently created
        """
        if id not in self.tasks.keys():
            pass