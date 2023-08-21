from task_manager import db
from sqlalchemy.orm import validates
import email_validator


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)    

    @validates('email')
    def validate_email(self, key, email):
        if not email:
            raise 
        ("Email address is required")
        
        try:
            email_validator.validate_email(email)
            return email
        except email_validator.EmailNotValidError as e:
            raise ValueError("Invalid email address")


class TaskModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable = False)
    created_at = db.Column(db.String, nullable=False)
    due_at = db.Column(db.String, nullable=False)
    updated_at = db.Column(db.String, nullable=False, default='not yet updtaed')
    is_completed = db.Column(db.Boolean, nullable =False) 
    description = db.Column(db.String)
    priority = db.Column(db.String, nullable=False)
    order = db.Column(db.Integer, nullable=False)
    
    


