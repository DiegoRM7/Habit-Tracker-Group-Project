
from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash, session
import re
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
# The above is used when we do login registration, flask-bcrypt should already be in your env check the pipfile

# Remember 'fat models, skinny controllers' more logic should go in here rather than in your controller. Your controller should be able to just call a function from the model for what it needs, ideally.
class Gym:
    db = "habit_tracker_schema"
    def __init__(self, data):
        self.id = data['gym_id']
        self.reps = data['reps']
        self.hours = data['hours']
        self.gym_start = data['gym_start']
        self.gym_stop = data['gym_stop']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id['user_id']
        self.gym_user = None
   
   
    # Create gym Models
   
    @classmethod
    def create_gym_habit(cls,gym_data):
        query = """
                INSERT INTO gym (reps, hours, gym_start, gym_stop, user_id)
                VALUES (%(reps)s, %(hours)s, %(gym_start)s, %(gym_stop)s, %(user_id)s)
                ;"""
        gym_id = connectToMySQL(cls.db).query_db(query, gym_data)
        print("gym_id:",gym_id)
        print(query)
        return gym_id

    # Read gym Models
    
    @classmethod
    def get_all_gym_habits(cls):
        query = """
                SELECT *
                FROM gym
                ;"""
        results = connectToMySQL(cls.db).query_db(query)
        gym_habit = []
        for a_gym_habit in results:
            gym_habit.append(cls(a_gym_habit))
        return gym_habit
        
    @classmethod
    def get_all_gym_habits_with_user_by_user_id(cls, user_id):
        query = """
                SELECT * FROM gym 
                JOIN user 
                ON user.id = gym.user_id 
                WHERE gym.user_id = %(user_id)s;
                ;"""
        results = connectToMySQL(cls.db).query_db(query, user_id)
        return results
# ! Uriah: works in mySQL, need to test in flask ^
    # Update gym Models
    
    # Delete gym Models
        
    #Gym Validation

    @staticmethod
    def validate_user_gym_habits(data):
        reps_regex = re.compile(r'^[1-9]\d*$')
        is_valid = True
        if not reps_regex.match(data['reps']):
            flash("Failed rep? Please enter a rep count greater than 0, or decrease the weigh until you can manage one repitition")
            is_valid = False
        return is_valid
        
        # ! Uriah: validate hours, gym start/stop with same regex? might need another regex to ensure proper time inputs(start/stop)