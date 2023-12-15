""""this file is going to be the users controllers file"""
"""all routes and controllers have been added in its entirely"""
from flask import render_template
from flask_app import app


@app.get("/")
def register():
    return "register template"


@app.get("/login")
def login():
    return "login template"


@app.get("/welcome")
def welcome():
    return "welcome template"


@app.get("/habit details")
def habitdetails():
    return "habit details template"


@app.get("/update")
def update():
    return "update template"


@app.get("/account details")
def accountdetails():
    return "account details template"


@app.get("/create habit")
def createhabit():
    return "create habit template"
