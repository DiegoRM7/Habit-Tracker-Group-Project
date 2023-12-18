
""""this file is going to be the users controllers file"""
"""all routes and controllers have been added in its entirely"""
from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models import user # import entire file, rather than class, to avoid circular imports
# As you add model files add them the the import above
# This file is the second stop in Flask's thought process, here it looks for a route that matches the request

@app.get("/")
def register():
    return render_template("register.html")

@app.post('/register/user')
def create_user():
    if user.User.create_user(request.form):
        return redirect("/dashboard")
    return redirect("/")

@app.get("/login")
def login():
    return render_template("login.html")

@app.post("/login/user")
def user_login():
    if user.User.login(request.form):
        return redirect("/dashboard")
    return redirect("/login")

# Update Users Controller (update users account info = password, username, location, email, first/last name's)
# Delete Users Controller (delete account button)

# todo: these habit routes need to be put into a separate habit controller

@app.get("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.get("/habit details")
def habitdetails():
    return "habit details template"

@app.get("/habit/update")
def update_habit_page():
    return render_template("update_habit.html")

@app.get("/account details")
def accountdetails():
    return "account details template"

@app.get("/habit/create")
def create_habit_page():
    return render_template("create_habit.html")








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