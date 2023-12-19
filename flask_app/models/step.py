
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
        self.step_id = data['step_id']
        self.first_name = data['amount']
        self.last_name = data['location']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']

#?? Create Step Models
    @classmethod
    def create_step_habit(cls,step_data):
        query = """
                INSERT INTO steps (amount, location, user_id)
                VALUES (%(amount)s, %(location)s, %(user_id)s)
                ;"""
        step_id = connectToMySQL(cls.db).query_db(query,step_data)
        return step_id

#?? Read Step Models

    @classmethod
    def get_step_habit_by_habit_id(cls,step_id):
        query = """
                SELECT *
                FROM steps 
                WHERE step_id = %(step_id)s
                ;"""
        results = connectToMySQL(cls.db).query_db(query, {"step_id" : step_id})
        return cls(results)

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
    
#?? Update Step Models
    @classmethod
    def update_steps(cls, data):
        # ! add validations when ready
        # ! check logged in user for increased route security?
        query = """
                UPDATE steps
                SET
                amount = %(amount)s,
                location = %(location)s,
                WHERE steps_id = %(steps_id)s;
                """
        return connectToMySQL(cls.db).query_db(query,data)
        # ! will eventually return True for validation purposes

#?? Delete Step Models
    @classmethod
    def delete_steps(cls,steps_id):
        # ! add validations when ready
        # ! check logged in user for increased route security?
        query = """
                DELETE FROM steps
                WHERE steps_id = %(steps_id)s;
                """
        return connectToMySQL(cls.db).query_db(query, {'steps_id' : steps_id})
        # ! will eventually return True for validation purposes
    
    #?? Step Validation

    @staticmethod
    def validate_step_habits(data):
        pass
    # todo regex for step amount to exclude negative int including 0
    # todo restrict location > 0 < 50 characters? Do we find regex to exclude numbers and unique characters?