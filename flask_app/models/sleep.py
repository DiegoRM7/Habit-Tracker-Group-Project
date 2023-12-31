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
        self.sleep_id = data["sleep_id"]
        self.hours = data["hours"]
        self.quality = data["quality"]
        self.sleep_start = data["sleep_start"]
        self.sleep_stop = data["sleep_stop"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.user_id = data["user_id"]  # user that's tracking their sleep

    # ? Create
    @classmethod
    def create_sleep_habit(cls, sleep_data):
        if not cls.validate_user_sleep_habits(sleep_data):
            return False
        query = """
                INSERT INTO sleep (hours, quality, sleep_start, sleep_stop, user_id)
                VALUES (%(hours)s, %(quality)s, %(sleep_start)s, %(sleep_stop)s, %(user_id)s)
                ;"""
        sleep_id = connectToMySQL(cls.db).query_db(query, sleep_data)
        print(sleep_id)
        return sleep_id

    # ? Read
    @classmethod
    def get_one_sleep_by_sleep_id(cls, sleep_id):  # to show on view page
        query = """
                SELECT *
                FROM sleep 
                WHERE sleep_id = %(sleep_id)s;
                """
        results = connectToMySQL(cls.db).query_db(query, {"sleep_id": sleep_id})
        print(results[0])
        return cls(results[0])

    @classmethod
    def get_all_sleep_habits(
        cls,
    ):  # for one table in the dashboard going to be used after mvp
        query = """
                SELECT * 
                FROM sleep
                ORDER BY created_at DESC;
                """
        results = connectToMySQL(cls.db).query_db(query)
        sleep_habit = []
        for a_sleep_habit in results:
            sleep_habit.append(cls(a_sleep_habit))
        return sleep_habit

    @classmethod
    def get_all_sleep_habits_by_user_id(
        cls, user_id
    ):  # for one table in the dashboard NOW
        query = """
                SELECT * FROM sleep
                JOIN user
                ON user.id = sleep.user_id
                WHERE sleep.user_id = %(user_id)s;
                """
        results = connectToMySQL(cls.db).query_db(query, {"user_id": user_id})
        if not results:
            return []
        return results

    # ? Update
    @classmethod
    def update_sleep(cls, data):
        # ! add validations when ready
        # ! check logged in user for increased route security?
        query = """
                UPDATE sleep
                SET
                hours = %(hours)s,
                quality = %(quality)s
                WHERE sleep_id = %(sleep_id)s;
                """
        return connectToMySQL(cls.db).query_db(query, data)
        # ! will eventually return True for validation purposes

    # ? Delete
    @classmethod
    def delete_sleep(cls, sleep_id):
        # ! add validations when ready
        # ! check logged in user for increased route security?
        query = """
                DELETE FROM sleep
                WHERE sleep_id = %(sleep_id)s;
                """
        return connectToMySQL(cls.db).query_db(query, {"sleep_id": sleep_id})
        # ! will eventually return True for validation purposes

    # ? Validation
    @staticmethod
    def validate_user_sleep_habits(data):
        is_valid = True
        if data["hours"]:
            if int(data["hours"]) < 1:
                flash(
                    "Not enough hours slept, please enter a tracked sleep session over 0 hours.",
                    "creating_sleep_habit",
                )
                is_valid = False
        if not data["hours"]:
            flash("No hours entered", "creating_sleep_habit")
            is_valid = False
        if data["quality"]:
            if int(data["quality"]) < 1:
                flash(
                    "quality must be great than 0, please enter a whole number",
                    "creating_sleep_habit",
                )
                is_valid = False
        if not data["quality"]:
            flash("No quality entered!", "creating_sleep_habit")
            is_valid = False
        # ?? tested and error occurring when creating a gym habit and same for the sleep habit
        # if data["sleep_start"]:
        #     if int(data["sleep_start"]) < 1:
        #         flash(
        #             "must enter time to track sleep_start, please enter a tracked sleep session over 0 hours.",
        #             "creating_sleep_habit",
        #         )
        #         is_valid = False
        if not data["sleep_start"]:
            flash("No sleep start time entered", "creating_sleep_habit")
            is_valid = False
        # ?? tested and error occurring when creating a gym habit and same for the sleep habit
        # if data["sleep_stop"]:
        #     if int(data["sleep_stop"]) < 1:
        #         flash(
        #             "Not enough hours slept, please enter a tracked sleep session over 0 hours.",
        #             "creating_sleep_habit",
        #         )
        #         is_valid = False
        if not data["sleep_stop"]:
            flash("No sleep stop time entered", "creating_sleep_habit")
            is_valid = False
        return is_valid

    # todo quality input type int (1-5 rating scale)
    # todo  hours int: 1-24(exclude negative int and 0)
    # todo copy datetime regex from gym validation?
