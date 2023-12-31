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
        self.amount = data['amount']
        self.location = data['location']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']

# ? Create
    @classmethod
    def create_step_habit(cls,step_data):
        if not cls.validate_step_habits(step_data):
            return False
        query = """
                INSERT INTO steps (amount, location, user_id)
                VALUES (%(amount)s, %(location)s, %(user_id)s)
                """
        step_id = connectToMySQL(cls.db).query_db(query,step_data)
        return step_id

# ? Read
    @classmethod
    def get_one_step_by_step_id(cls,step_id): # to show in view habit page
        query = """
                SELECT *
                FROM steps 
                WHERE step_id = %(step_id)s;
                """
        results = connectToMySQL(cls.db).query_db(query, {"step_id": step_id})
        print(results[0])
        return cls(results[0])

    @classmethod
    def get_all_step_habits(cls): # used for dashboard after MVP
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
    def get_all_step_habits_by_user_id(cls, user_id): # for dashboard table NOW working
        query = """
                SELECT * FROM steps
                JOIN user
                ON user.id = steps.user_id
                WHERE steps.user_id = %(user_id)s
                """
        results = connectToMySQL(cls.db).query_db(query,{"user_id": user_id})
        if not results:
            return []
        return results

# ? Update
    @classmethod
    def update_steps(cls, data):
        query = """
                UPDATE steps
                SET
                amount = %(amount)s,
                location = %(location)s
                WHERE step_id = %(step_id)s;
                """
        return connectToMySQL(cls.db).query_db(query, data)
        # ! will eventually return True for validation purposes

# ? Delete
    @classmethod
    def delete_steps(cls,step_id):
        query = """
                DELETE FROM steps
                WHERE step_id = %(step_id)s;
                """
        return connectToMySQL(cls.db).query_db(query, {'step_id' : step_id})
    
# ? Validation
    @staticmethod
    def validate_step_habits(data):
        STEP_LOCATION_REGEX = re.compile(r'^[^-0-9]+$')
        is_valid = True
        # amount
        if data["amount"]:
            if int(data['amount']) < 1:
                flash("Please enter a step amount greater than 0, lets go knees to chest!!!","creating_steps_habit")
                is_valid = False
        if not data["amount"]:
            flash("Please enter an amount, it was blank.","creating_steps_habit")
            is_valid = False
        #  location
        if data["location"]:
            if len(data['location']) < 2 :
                flash("Please enter the location your steps occurred","creating_steps_habit")
                is_valid = False
        if not data["location"]:
            flash("No location entered, please write one!","creating_steps_habit")
            is_valid = False
        if not STEP_LOCATION_REGEX.match(data['location']):
            is_valid = False
        return is_valid
