
from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash, session
import re
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
# The above is used when we do login registration, flask-bcrypt should already be in your env check the pipfile

# Remember 'fat models, skinny controllers' more logic should go in here rather than in your controller. Your controller should be able to just call a function from the model for what it needs, ideally.

class Step:
    db = "habit_tracker_schema"
    def __init__(self, data):
        self.id = data['gym_id']
        self.first_name = data['reps']
        self.last_name = data['hours']
        self.email = data['gym_start']
        self.password = data['gym_stop']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id['user_id']
        self.step_user = None

    # Create Step Models
    @classmethod
    def create_step_habit(cls,step_data):
        query = """
                INSERT INTO steps (amount, location, user_id)
                VALUES (%(amount)s, %(location)s, %(user_id)s)
                ;"""
        step_id = connectToMySQL(cls.db).query_db(query,step_data)
        print("step_id:",step_id)
        return step_id

    # Read Step Models
    @classmethod
    def get_all_step_habits(cls):
        query = """
                SELECT * 
                FROM steps
                ;"""
        results = connectToMySQL(cls.db).query_db(query)
        step_habit = []
        for a_step_habit in results:
            step_habit.append(cls(a_step_habit))
        return step_habit
    
    @classmethod
    def get_all_step_habits_with_user_by_user_id(cls,user_id):
        query = """
                SELECT * FROM steps
                JOIN user
                ON user.id = step.user_id
                WHERE step.user_id = %(user_id);
                """
        results = connectToMySQL(cls.db).query_db(query,{"user_id": user_id})
        return results
    
    # Update Step Models

    # Delete Step Models

    # Step Validation
    @staticmethod
    def validate_step_habits(data):
        pass
    # todo regex for step amount to exclude negative int including 0
    # todo restrict location > 0 < 50 characters? Do we find regex to exclude numbers and unique characters?