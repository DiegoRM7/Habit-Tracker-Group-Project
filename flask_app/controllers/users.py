
""""this file is going to be the users controllers file"""
"""all routes and controllers have been added in its entirely"""
from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models import user, sleep, gym, step # import entire file, rather than class, to avoid circular imports
# As you add model files add them the the import above
# This file is the second stop in Flask's thought process, here it looks for a route that matches the request

@app.get("/")
def register():
    return render_template("register.html")

@app.post('/register/user')
def create_user():
    if not user.User.validate_user_registration(request.form):
        return redirect("/")
    if user.User.create_user(request.form):
        return redirect("/dashboard", sleep_data = sleep.Sleep.get_all_sleep_habits())
    print("There was an error creating a user for some reason")
    return redirect("/")

@app.get("/dashboard")
def dashboard():
    if 'user_id' not in session:
        return redirect('/login')
    # sleep_data = sleep.Sleep.get_all_sleep_habits()
    # user_info = user.User.get_user_by_user_id_logged_in('user_id')
    all_gym_habits = gym.Gym.get_all_gym_habits_with_user_by_user_id(session["user_id"])
    all_sleep_habits = sleep.Sleep.get_all_sleep_habits_by_user_id(session["user_id"])
    all_step_habits = step.Step.get_all_step_habits_by_user_id(session["user_id"])
    return render_template("dashboard.html", all_gym_habits = all_gym_habits, all_sleep_habits = all_sleep_habits, all_step_habits = all_step_habits)

@app.get("/login")
def login():
    return render_template("login.html")

@app.post("/login/user")
def user_login():
    if user.User.login(request.form):
        return redirect("/dashboard")
    return redirect("/login")

@app.get("/logout")
def logout():
    session.clear()
    flash("You've logged out successfully!","logout_account")
    return redirect("/login")
# Update Users Controller (update users account info = password, username, location, email, first/last name's)
# Delete Users Controller (delete account button)





# Notes:
# 1 - Use meaningful names
# 2 - Do not overwrite function names
# 3 - No matchy, no worky
# 4 - Use consistent naming conventions 
# 5 - Keep it clean
# 6 - Test every little line before progressing
# 7 - READ ERROR MESSAGES!!!!!!
# 8 - Error messages are found in the browser and terminal




# How to use path variables:
# @app.route('/<int:id>')                                   The variable must be in the path within angle brackets
# def index(id):                                            It must also be passed into the function as an argument/parameter
#     user_info = user.User.get_user_by_id(id)              The it will be able to be used within the function for that route
#     return render_template('index.html', user_info)

# Converter -	Description
# string -	Accepts any text without a slash (the default).
# int -	Accepts integers.
# float -	Like int but for floating point values.
# path 	-Like string but accepts slashes.

# Render template is a function that takes in a template name in the form of a string, then any number of named arguments containing data to pass to that template where it will be integrated via the use of jinja
# Redirect redirects from one route to another, this should always be done following a form submission. Don't render on a form submission.