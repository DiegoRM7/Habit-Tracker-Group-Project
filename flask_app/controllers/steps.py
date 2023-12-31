""""this file is going to be the sleep controllers file"""
"""all routes and controllers have been added in its entirely"""
from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models import step # import entire file, rather than class, to avoid circular imports
# As you add model files add them the the import above
# This file is the second stop in Flask's thought process, here it looks for a route that matches the request

@app.post("/habit/create/steps/process")
def create_step_habit_form_process():
    if 'user_id' not in session:
        return redirect('/')
    if step.Step.create_step_habit(request.form):
        print("step habit was created! Should be redirect to dashboard") #convert to flash when ready
        return redirect("/dashboard")
    # will redirect to ("/habit/details") later on when we have page made
    return redirect("/habit/create")

#? now on gym controller to route for all type of habits in one route based on(habit_type/habit_id)
# @app.post("/habit/update/steps/process")
# def update_habit_form_process():
#     if 'user_id' not in session:
#         return redirect('/')
#     if step.Step.validate_step_habits(request.form):
#         step.Step.update_steps(request.form)
#         return redirect("/habit/update")
#     return redirect("/habit/update")






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