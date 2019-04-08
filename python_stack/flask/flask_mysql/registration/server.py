from flask import Flask, redirect, render_template, session, flash, request
from sqlconnection import connectToMySQL
from flask_bcrypt import Bcrypt    
import re

app = Flask(__name__)
app.secret_key = 'Such Secret'
bcrypt = Bcrypt(app)

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():

    pw_hash = bcrypt.generate_password_hash(request.form['password'])

    if len(request.form['first_name']) < 1:
        flash('First name required!')
    if len(request.form['last_name']) < 1:
        flash('Last name required!')
    if request.form['password'] != request.form['confirm_password']:
        flash('Passwords must match!')
    if not EMAIL_REGEX.match(request.form['email']):    
        flash("Invalid email address!")    

    if not '_flashes' in session.keys():
        db = connectToMySQL('registration')        

        query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (%(fn)s, %(ln)s, %(em)s, %(pw)s, now(), now());"
    
        data = {
            'fn': request.form['first_name'],
            'ln': request.form['last_name'],
            'pw': pw_hash,
            'em': request.form['email']
        }

        new_id = db.query_db(query, data)
        flash('Submission Successful!')
    return redirect('/')

@app.route('/login', methods=['POST'])
def login():
    db = connectToMySQL('registration')
    query = 'SELECT * from users where email = %(em)s'
    data = {
        'em': request.form['email']
    }

    results = db.query_db(query, data)
    if results:
        if bcrypt.check_password_hash(results[0]['password'], request.form['password']):
            session['userid'] = results[0]['email']
            flash('Successful log in!')
            return redirect('/success')
        else:
            flash('You could not be logged in!')
            return redirect('/')
    else:
        flash('User not found!')
        return redirect('/')

@app.route('/success')
def success():
    if not 'userid' in session.keys():
        flash('You must log in to see this page!')
        return redirect('/')
    else:    
        return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')    

if __name__ == '__main__':
    app.run(debug=True)