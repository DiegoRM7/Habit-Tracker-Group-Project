
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

    # Create Sleeps Models
    

    # Read Sleep Models
        
        
    # Update Sleep Models
    
    # Delete Sleep Models
        
    # Sleep Validation
