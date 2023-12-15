from flask_app import app
from flask_app.controllers import users #controllers go here, if you add a new controller file you have to also add it here
# This is where Flask's thought process starts. The request enters here, then goes to the controller above which has a matching route.

if __name__=="__main__":   
    app.run(debug=True) 
    # On line six you can change the port number.

# debug needs to be set to False when deployed.
# We shared a video showing how the information leaked by this feature and help hackers.