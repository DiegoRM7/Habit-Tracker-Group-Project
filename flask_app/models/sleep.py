
from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash, session
import re
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
# The above is used when we do login registration, flask-bcrypt should already be in your env check the pipfile

# Remember 'fat models, skinny controllers' more logic should go in here rather than in your controller. Your controller should be able to just call a function from the model for what it needs, ideally.

class Sleep:
    db = "habit_tracker_schema"
    def __init__(self, data):
        self.sleep_id = data['sleep_id']
        self.hours = data['hours']
        self.quality = data['quality']
        self.sleep_start = data['sleep_start']
        self.sleep_stop = data['sleep_stop']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id['user_id']
        self.sleep_user = None

    # Create Sleeps Models
    @classmethod
    def create_sleep_habit(cls,sleep_data):
        query = """
                INSERT INTO sleep (hours, quality, sleep_start, sleep_stop, user_id)
                VALUES (%(hours)s, %(quality)s, %(sleep_start)s, %(sleep_stop)s, %(user_id)s)
                ;"""
        sleep_id = connectToMySQL(cls.db).query_db(query, sleep_data)
        print("sleep_id:",sleep_id)
        print(query)
        return sleep_id

    # Read Sleep Models
    @classmethod 
    def get_all_sleep_habits(cls):
        query = """
                SELECT * 
                FROM sleep
                ;"""
        results = connectToMySQL(cls.db).query_db(query)
        sleep_habit = []
        for a_sleep_habit in results:
            sleep_habit.append(cls(a_sleep_habit))
        return sleep_habit
    
    @classmethod 
    def get_all_sleep_habits_with_user_by_user_id(cls, user_id):
        query = """
                SELECT * FROM sleep
                JOIN user
                ON user.id = sleep.user_id
                WHERE gym.user_id = %(user_id)s;
                ;"""
        results = connectToMySQL(cls.db).query_db(query,user_id)
        return results
# ! Uriah: works in mySQL, need to test in flask ^

        
    # Update Sleep Models
    
    # Delete Sleep Models
        
    # Sleep Validation
    @staticmethod
    def validate_user_sleep_habits(data):
        pass
    # todo quality input type int (1-5 rating scale)
    # todo  hours int: 1-24(exclude negative int and 0)
    # todo copy datetime regex from gym validation?