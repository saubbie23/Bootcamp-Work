from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from flask_migrate import Migrate

app = Flask(__name__)

# configurations to tell our app about the database we'll be connecting to
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

migrate = Migrate(app, db)

class Dojos(db.Model):
    __tablename__ = "dojos"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45))
    city = db.Column(db.String(45))
    state = db.Column(db.String(45))
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())

class Users(db.Model):
    __table_name = "users"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(45))
    last_name = db.Column(db.String(45))
    dojo_id = db.Column(db.Integer, db.ForeignKey('dojos.id'), nullable=False)
    dojo = db.relationship('Dojos', foreign_keys=[dojo_id], backref="user_dojo", cascade="all")


@app.route('/')
def index():
    dojos = Dojos.query.all()
    
    return render_template('index.html', dojos=dojos)

@app.route('/add_dojo', methods=["POST"])
def add_dojo():
    new_dojo = Dojos(name= request.form['dojo_name'], city= request.form['dojo_city'], state= request.form['dojo_state'])
    db.session.add(new_dojo)
    db.session.commit()

    return redirect('/')

@app.route('/add_user', methods=["POST"])
def add_student():
    dojo_name = request.form['dojo']    
    dojo_key = Dojos.query.filter_by(name=dojo_name) 
   
    new_student = Users(first_name= request.form['first_name'], last_name= request.form['last_name'], dojo_id= dojo_key[0].id)
    db.session.add(new_student)
    db.session.commit()

    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)