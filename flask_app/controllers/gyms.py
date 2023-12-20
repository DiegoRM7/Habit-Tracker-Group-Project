""""this file is going to be the gym controllers file"""
"""all routes and controllers have been added in its entirely"""
from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models import gym, user # import entire file, rather than class, to avoid circular imports
# As you add model files add them the the import above
# This file is the second stop in Flask's thought process, here it looks for a route that matches the request

@app.get("/habit/details")
def habit_details():
    if 'user_id' not in session:
        return redirect('/')
    user_info = user.User.get_user_by_user_id_logged_in('user_id')
    print(user_info["first_name"])
    return render_template("habit_details.html", user_info = user_info)

@app.get("/habit/update")
def update_habit_page():
    if 'user_id' not in session:
        return redirect('/')
    return render_template("update_habit.html")

@app.get("/account/details")
def account_details():
    if 'user_id' not in session:
        return redirect('/')
    return "account details template"

@app.get("/habit/create")
def create_habit_page():
    if 'user_id' not in session:
        return redirect('/')
    return render_template("create_habit.html")

@app.post("/habit/create/gym/process")
def create_gym_habit_form_process():
    if 'user_id' not in session:
        return redirect('/')
    if gym.Gym.create_gym_habit(request.form):
        print("\ngym habit got created successfully\n")
        return redirect(f'/habit/details/{request.form["habit_id"]}')
    return redirect("/habit/create")








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