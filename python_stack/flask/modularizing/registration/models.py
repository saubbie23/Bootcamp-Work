from sqlalchemy.sql import func
from config import db, bcrypt
from flask import flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class Users(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key= True)
    first_name = db.Column(db.String(45))
    last_name = db.Column(db.String(45))
    email = db.Column(db.String(255))
    password = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())

    @classmethod
    def validate_user(cls, user_data):
        is_valid = True
        if len(user_data['first_name']) < 1:
            flash('First name required!')
            is_valid = False
        if len(user_data['last_name']) < 1:
            flash('Last name required!')
            is_valid = False
        if user_data['password'] != user_data['confirm_password']:
            flash('Passwords must match!')
            is_valid = False
        if not EMAIL_REGEX.match(user_data['email']):    
            flash("Invalid email address!")
            is_valid = False    

        return is_valid

    @classmethod
    def add_user(cls, user_data):
        hashed_pw = bcrypt.generate_password_hash(user_data["password"])
        new_user = cls(first_name= user_data["first_name"], last_name= user_data["last_name"], email= user_data["email"], password= hashed_pw)

        db.session.add(new_user)
        db.session.commit()
        return new_user

    @classmethod
    def login(cls, form_data):
        success = False
        user_info = Users.query.filter_by(email=form_data["email"])

        if bcrypt.check_password_hash(user_info[0].password, form_data["password"]):
            success = True
        else:
            flash('Incorect username/password combination!')

        return success

    @classmethod
    def getID(cls, form_data):
        user_info = Users.query.filter_by(email=form_data["email"])
        user = [user_info[0].id, user_info[0].email]

        return user