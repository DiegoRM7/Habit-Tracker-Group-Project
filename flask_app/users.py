""""this file is going to be the users controllers file"""
from flask import render_template
from flask_app import app


@app.get("/")
def register():
    return "register template"


@app.get("/login")
def login():
    return "login template"
