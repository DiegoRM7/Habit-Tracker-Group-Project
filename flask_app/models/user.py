from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash, session
import re
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)
# The above is used when we do login registration, flask-bcrypt should already be in your env check the pipfile

# Remember 'fat models, skinny controllers' more logic should go in here rather than in your controller. Your controller should be able to just call a function from the model for what it needs, ideally.


class User:
    db = "habit_tracker_schema"

    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.username = data["username"]
        self.location = data["location"]
        self.email = data["email"]
        self.password = data["password"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.gym = []  # holds all the gym habit tracked sessions for this user
        self.sleep = []  # sleep habit tracked sessions
        self.step = []  # step habit tracked sessions

    # Create Users Models
    @classmethod
    def create_user(cls,user_data):
        if not cls.validate_user_registration(user_data):
            return False
        user_data = user_data.copy()
        user_data["password"] = bcrypt.generate_password_hash(user_data["password"])
        query = """
                INSERT INTO user (first_name, last_name, username, location, email, password)
                VALUES (%(first_name)s, %(last_name)s, %(username)s, %(location)s, %(email)s, %(password)s)
                ;"""
        user_id = connectToMySQL(cls.db).query_db(query, user_data)
        session["user_id"] = user_id
        session["first_name"] = user_data["first_name"]
        # When user successfully logs in first_name and user_id are put into session for security and UI purposes.
        return user_id

    # Read Users Models
    @classmethod
    def get_user_by_email(cls, email):
        query = """
                SELECT *
                FROM user
                WHERE email = %(email)s;
                """
        result = connectToMySQL(cls.db).query_db(query, {"email": email})
        if result:
            this_user = cls(result[0])
            return this_user
        return False

    @classmethod
    def get_user_by_user_id_logged_in(cls, user_id):
        query = """
                SELECT *
                FROM user
                WHERE id = %(user_id)s;
                """
        result = connectToMySQL(cls.db).query_db(query, {"user_id": user_id})
        return result[0]
    
    @classmethod
    def login(cls, data):
        this_user = User.get_user_by_email(data['email'])
        if this_user:
            if bcrypt.check_password_hash(this_user.password, data["password"]):
                session["user_id"] = this_user.id
                session["first_name"] = this_user.first_name
                # could also save username into session here as well
                return True
            # edited to make flash show when specifically called on login page
        flash("Invalid Login Information", "no_user_shown_in_DB")
        return False

    # user_validation
    @staticmethod
    def validate_user_registration(data):
        EMAIL_REGEX = re.compile(r"^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$")
        is_valid = True
        if len(data["email"]) < 1:
            flash("Email required", "register_validation")
            is_valid = False
        if not EMAIL_REGEX.match(data["email"]):
            flash("Invalid email", "register_validation")
            is_valid = False
        if User.get_user_by_email(data["email"]):
            flash("Email taken", "register_validation")
        if len(data["location"]) < 2:
            flash("Please provide Location", "register_validation")
            is_valid = False
        if len(data["first_name"]) < 2:
            flash("First Name must be at least 2 characters", "register_validation")
            is_valid = False
        if len(data["last_name"]) < 2:
            flash("Last Name be at least 2 characters", "register_validation")
            is_valid = False
        if len(data["password"]) < 8:
            flash("Password must be at least 8 characters", "register_validation")
            is_valid = False
        if data["password"] != data["confirm_password"]:
            flash("Passwords must match", "register_validation")
            is_valid = False
        return is_valid
