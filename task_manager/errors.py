from task_manager import app              
from flask_restful import abort

class EmailAlreadyExistsError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class InvalidEmailError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)



@app.errorhandler(EmailAlreadyExistsError)
def handle_email_exists_error(error):  
    abort(409, message=error.message)     

@app.errorhandler(InvalidEmailError)
def handle_invalid_email_error(error):
    abort(409, message=error.message)            