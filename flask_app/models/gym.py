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
        self.gym_id = data["gym_id"]
        self.reps = data["reps"]
        self.hours = data["hours"]
        self.gym_start = data["gym_start"]
        self.gym_stop = data["gym_stop"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.user_id = data["user_id"]  # user that's tracking their gym session

    # ? Create
    @classmethod
    def create_gym_habit(cls, gym_data):
        if not cls.validate_user_gym_habits(gym_data):
            return False
        query = """
                INSERT INTO gym (reps, hours, gym_start, gym_stop, user_id)
                VALUES (%(reps)s, %(hours)s, %(gym_start)s, %(gym_stop)s, %(user_id)s)
                ;"""
        gym_id = connectToMySQL(cls.db).query_db(query, gym_data)
        if not gym_id:
            return []
        return gym_id

    # ? Read
    @classmethod
    def get_one_gym_by_gym_id(cls, gym_id):  # to show on habit detail page
        query = """
                SELECT *
                FROM gym 
                WHERE gym_id = %(gym_id)s;
                """
        results = connectToMySQL(cls.db).query_db(query, {"gym_id": gym_id})
        print(f"{results[0]}\n")
        return cls(results[0])

    @classmethod
    def get_all_gym_habits(
        cls,
    ):  # for one table in the dashboard going to be used after mvp
        query = """
                SELECT *
                FROM gym
                ORDER BY created_at DESC;
                """
        results = connectToMySQL(cls.db).query_db(query)
        gym_habit = []
        for a_gym_habit in results:
            gym_habit.append(cls(a_gym_habit))
        return gym_habit

    @classmethod
    def get_all_gym_habits_with_user_by_user_id(
        cls, user_id
    ):  # for one table in the dashboard
        query = """
                SELECT * FROM gym 
                JOIN user 
                ON user.id = gym.user_id 
                WHERE gym.user_id = %(user_id)s;
                """
        results = connectToMySQL(cls.db).query_db(query, {"user_id": user_id})
        if not results:
            return []
        return results

    # ! Uriah: works in mySQL, need to test in flask ^

    # ? Update
    @classmethod
    def update_gym(cls, data):
        # ! add validations when ready
        query = """
                UPDATE gym
                SET
                reps = %(rep)s,
                hours = %(hours)s,
                gym_start = %(gym_start)s,
                gym_stop = %(gym_stop)s,
                WHERE gym_id = %(gym_id)s;
                """
        return connectToMySQL(cls.db).query_db(query, data)

    # ? Delete
    @classmethod
    def delete_gym(cls, gym_id):
        # ! add validations when ready
        # ! check logged in user for increased route security?
        query = """
                DELETE FROM gym
                WHERE gym_id = %(gym_id)s;
                """
        return connectToMySQL(cls.db).query_db(query, {"gym_id": gym_id})
        # ! will eventually return True for validation purposes

    # ? Gym_Validation
    @staticmethod
    def validate_user_gym_habits(data):
        DATE_TIME_REGEX = re.compile(r"^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}$")
        is_valid = True
        if data["reps"]:
            if int(data["reps"]) < 1:
                flash(
                    "Failed rep? Please enter a rep count greater than 0, or decrease the weight until you can manage one repitition",
                    "creating_gym_habit",
                )
                is_valid = False
        if not data["reps"]:
            flash("No rep range entered", "creating_gym_habit")
            is_valid = False
        if data["hours"]:
            if int(data["hours"]) < 1:
                flash(
                    "hours must be great than 0, please enter a whole number",
                    "creating_gym_habit",
                )
                is_valid = False
        if not data["hours"]:
            flash("No hours entered!", "creating_gym_habit")
            is_valid = False
        if data["gym_start"]:
            if int(data["gym_start"]) < 1:
                flash(
                    "hours must be greater than 0, please enter a whole number",
                    "creating_gym_habit",
                )
                is_valid = False
        if not data["gym_start"]:
            flash("No gym start entered!", "creating_gym_habit")
            is_valid = False
        if not data["gym_stop"]:
            flash("No gym stop entered!", "creating_gym_habit")
            is_valid = False
        elif data["gym_stop"]:
            if int(data["gym_stop"]) < 1:
                flash(
                    "gym stop must be greater than 0, please enter a whole number",
                    "creating_gym_habit",
                )
                is_valid = False
        # ! missing to check if datetime for start / stop are empty or not
        # if not DATE_TIME_REGEX.match(['gym_start']):
        #     is_valid = False
        #     flash("Please enter a valid date/time for Time Started Gym Session")
        # if not DATE_TIME_REGEX.match(['gym_stop']):
        #     flash("Please enter a valid date/time for Time Ended Gym Session")
        #     is_valid = False
        return is_valid

        # ! Uriah: validate hours, gym start/stop with same regex? might need another regex to ensure proper time inputs(start/stop)
