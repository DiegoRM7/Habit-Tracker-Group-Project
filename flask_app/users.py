""""this file is going to be the users controllers file"""
from flask import render_template
from flask_app import app


@app.get("/")
def register():
    return "register template"


@app.get("/login")
def login():
    return "login template"


@app.get("/welcome")
def login():
    return "welcome template"


@app.get("/habit details")
def login():
    return "details template"


@app.get("/update")
def login():
    return "update template"


@app.get("/account details")
def login():
    return "account details template"


@app.get("/create habit")
def login():
    return "create habit template"
