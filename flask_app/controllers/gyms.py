""""this file is going to be the gym controllers file"""
"""all routes and controllers have been added in its entirely"""
from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models import gym, user, sleep, step # import entire file, rather than class, to avoid circular imports
# As you add model files add them the the import above
# This file is the second stop in Flask's thought process, here it looks for a route that matches the request

#? for habit type string, input this into each view jinja link respective to each habit type
@app.get("/habit/details/<string:habit_type>/<int:habit_id>")
def habit_details(habit_type, habit_id):
    if 'user_id' not in session:
        return redirect('/')
    # user_info = user.User.get_user_by_user_id_logged_in(session['user_id'])

    # with these if statements the user should be fed the appropriate data from the DB and display such things
    # show data query that will only get everything for a specific habit id
    # render_template to habit detail page still with respective habit details
    # habit_type would equal the name of habit (ex:gym) which then you can say in jinja if habit_type == gym -> [do this code]
    if habit_type == "gym":
        gym_habit = gym.Gym.get_one_gym_by_gym_id(habit_id)
        return render_template("habit_details.html", gym_habit = gym_habit, habit_type = habit_type, habit_id = habit_id)
    
    if habit_type == "sleep":
        sleep_habit = sleep.Sleep.get_one_sleep_by_sleep_id(habit_id)
        return render_template("habit_details.html", sleep_habit = sleep_habit, habit_type = habit_type, habit_id = habit_id)
    
    if habit_type == "steps":
        steps_habit = step.Step.get_one_step_by_step_id(habit_id)
        return render_template("habit_details.html", steps_habit = steps_habit, habit_type = habit_type, habit_id = habit_id)

#? only can get to by the habit details page that already is serving these two habit_values parameters
#! LOAD PAGE
@app.get("/habit/update/<string:habit_type>/<int:habit_id>")
def update_habit_page(habit_type, habit_id):
    if 'user_id' not in session:
        return redirect('/')
    
    # same concept as the routing that serves the habit details page above ^
    if habit_type == "gym":
        gym_habit = gym.Gym.get_one_gym_by_gym_id(habit_id)
        return render_template("update_habit.html", gym_habit = gym_habit, habit_type = habit_type, habit_id = habit_id)
    if habit_type == "sleep":
        sleep_habit = sleep.Sleep.get_one_sleep_by_sleep_id(habit_id)
        return render_template("update_habit.html", sleep_habit = sleep_habit, habit_type = habit_type, habit_id = habit_id)
    if habit_type == "steps":
        steps_habit = step.Step.get_one_step_by_step_id(habit_id)
        return render_template("update_habit.html", steps_habit = steps_habit, habit_type = habit_type, habit_id = habit_id)
    
#! PROCESS SUBMIT FORM
# same concept as the routing that serves the habit details page above ^
@app.post("/habit/update/process/<string:habit_type>/<int:habit_id>")
def update_habit_process_submitted(habit_type, habit_id):
    if 'user_id' not in session:
        return redirect('/')
    
    if habit_type == "gym":
        if gym.Gym.update_gym(request.form):
            flash(f"{habit_type.capitalize()} habit with {habit_type}_id { habit_id } has been updated!, success_habit_updated")
        gym_habit = gym.Gym.get_one_gym_by_gym_id(habit_id)
        return render_template("habit_details.html", gym_habit = gym_habit, habit_type = habit_type, habit_id = habit_id)
    if habit_type == "sleep":
        if sleep.Sleep.update_sleep(request.form):
            flash(f"{habit_type.capitalize()} habit with {habit_type}_id { habit_id } has been updated!, success_habit_updated")
        sleep_habit = sleep.Sleep.get_one_sleep_by_sleep_id(habit_id)
        return render_template("habit_details.html", sleep_habit = sleep_habit, habit_type = habit_type, habit_id = habit_id)
    if habit_type == "steps":
        if step.Step.update_steps(request.form):
            flash(f"{habit_type.capitalize()} habit with {habit_type}_id { habit_id } has been updated!, success_habit_updated")
        steps_habit = step.Step.get_one_step_by_step_id(habit_id)
        return render_template("habit_details.html", steps_habit = steps_habit, habit_type = habit_type, habit_id = habit_id)

@app.get("/account/details")
def account_details():
    if 'user_id' not in session:
        return redirect('/')
    
    user_info = user.User.get_user_by_user_id_logged_in(session['user_id'])
    gym_habits = gym.Gym.get_all_gym_habits_with_user_by_user_id(session["user_id"])
    sleep_habits = sleep.Sleep.get_all_sleep_habits_by_user_id(session["user_id"])
    steps_habits = step.Step.get_all_step_habits_by_user_id(session["user_id"])
    return render_template("account.html", gym_habits = gym_habits,  sleep_habits = sleep_habits, steps_habits = steps_habits, user_info = user_info)

#? set up for later to update user data
# @app.post("/account/update")
# def account_details():
#     if 'user_id' not in session:
#         return redirect('/')
#     return render_template("account.html")

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
        return redirect("/dashboard")
        # later will use return redirect(f'/habit/details/{request.form["habit_id"]}')
    return redirect("/habit/create")

# ? DELETE HABIT ROUTE
@app.get("/habit/delete/<string:habit_type>/<int:habit_id>")
def delete_habit(habit_type, habit_id):
    if habit_type == "gym":
        gym.Gym.delete_gym(habit_id)
        return redirect("/dashboard")
    if habit_type == "sleep":
        sleep.Sleep.delete_sleep(habit_id)
        return redirect("/dashboard")
    if habit_type == "steps":
        step.Step.delete_steps(habit_id)
        return redirect("/dashboard")








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