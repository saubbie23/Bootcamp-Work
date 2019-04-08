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

        db = connectToMySQL('registration')
        query = "SELECT * FROM users where id = " + str(new_id)
        results = db.query_db(query)
        session['userid'] = results[0]['email']
        session['first_name'] = results[0]['first_name']
        session['id'] = results[0]['id']
        return redirect('/success')
    else:
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
            session['first_name'] = results[0]['first_name']
            session['id'] = results[0]['id']
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
        db = connectToMySQL('registration') 
        query = "SELECT tweets.id, tweets.tweet, tweets.created_at, tweets.users_id, CONCAT(users.first_name, ' ', users.last_name) as user_name, count(tweets_id) as likes, follows.follower_id, follows.users_id as follower FROM users LEFT JOIN tweets on users.id = tweets.users_id LEFT JOIN likes on tweets.id = likes.tweets_id LEFT JOIN follows on users.id = follows.users_id WHERE tweets.id IS NOT NULL ORDER BY tweets.created_at desc"
        results = db.query_db(query)

        return render_template('/login.html', tweets=results)

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')  

@app.route('/submit_tweet', methods=['POST'])
def tweet():
    print(request.form)
    if len(request.form['tweet']) < 1 or len(request.form['tweet']) > 255:
        flash('Your tweet must be between 1 and 255 characters!')

    if not '_flashes' in session.keys():
        db = connectToMySQL('registration')
        query = 'INSERT INTO tweets (users_id, tweet, created_at, updated_at) VALUES(%(id)s, %(tw)s, now(), now());' 
        
        data = {
            'id': session['id'],
            'tw': request.form['tweet']        
            }
        
        new_tweet_id = db.query_db(query, data)
        return redirect('/success')
    else:
        return redirect('/success')    

@app.route('/tweets/<id>/add_like', methods=['POST'])
def add_like(id):
    db = connectToMySQL('registration')
    query = "SELECT * FROM likes where users_id = " + str(session['id']) + " and tweets_id = " + str(id)
    results = db.query_db(query)

    if results:
        flash("You already liked this tweet! Can't like it again!")
        return redirect('/success')


    db = connectToMySQL('registration')
    query = "INSERT INTO likes (users_id, tweets_id, created_at, updated_at) VALUES(%(id)s, %(tw)s, now(), now());"
    data = {
        'id': session['id'],
        'tw': int(id)
    }

    update_like = db.query_db(query, data)
    return redirect('/success')

@app.route('/tweets/<id>/delete', methods=['POST'])
def deleteTweet(id):
    db = connectToMySQL('registration')
    query = "DELETE FROM likes WHERE tweets_id = " + id
    delete_likes = db.query_db(query)

    db = connectToMySQL('registration')
    query = "DELETE FROM tweets where id = " + id
    delete_tweet = db.query_db(query)

    return redirect('/success')

@app.route('/tweets/<id>/edit')
def editTweet(id):
    db = connectToMySQL('registration')
    query = "SELECT tweet from tweets WHERE id = " + id
    result = db.query_db(query)

    return render_template('edit.html', id=id, results=result)


@app.route('/tweets/<id>/update', methods=['POST', 'GET'])
def updateTweet(id):
    if len(request.form['edit']) < 1 or len(request.form['edit']) > 255:
        flash('Your tweet must be between 1 and 255 characters!')

    if not '_flashes' in session.keys():
        db = connectToMySQL('registration')
        query = "UPDATE tweets set tweet = %(tw)s, updated_at = now() where id = " + id
        data = {'tw': request.form['edit']}

        updated = db.query_db(query, data)

        return redirect('/success')
    else:
        return redirect('/tweets/' + id + '/edit')

@app.route('/users')
def users():
    db = connectToMySQL('registration')
    query = "SELECT id, CONCAT(first_name, ' ', last_name) as name, email from users;"
    results = db.query_db(query)
    
    return render_template('users.html', users=results)

@app.route('/follow/<id>')
def addFollow(id):
    db = connectToMySQL('registration')
    query = "INSERT INTO follows (users_id, follower_id) VALUES(" + str(session['id']) + ", " + id + ");"
    new_follow = db.query_db(query)

    return redirect('/users')

if __name__ == '__main__':
    app.run(debug=True)