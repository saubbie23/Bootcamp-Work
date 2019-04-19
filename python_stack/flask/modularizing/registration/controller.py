from flask import render_template, redirect, request, session, flash
from models import Users

def index():
    return render_template('index.html')

def register():
    validation = Users.validate_user(request.form)

    if not validation:
        return redirect('/')
    else:
        new_user = Users.add_user(request.form)
        session["user_id"] = new_user.id
    return redirect('/')

def login():
    login = Users.login(request.form)

    if not login:
        return redirect('/')
    else:
        user = Users.getID(request.form)
        session["user_id"] = user[0]
        session["user_name"] = user[1]
        return redirect('/success')

def success():
    if not "user_id" in session.keys():
        flash("You must log in to see this page!")
        return redirect('/')
    else:
        return render_template('login.html')

def logout():
    session.clear()
    return redirect('/')