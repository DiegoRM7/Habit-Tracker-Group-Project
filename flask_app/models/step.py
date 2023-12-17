
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

    # Create Step Models
        

    # Read Step Models
        
        
    # Update Step Models
    
    # Delete Step Models
        
    # Step Validation
