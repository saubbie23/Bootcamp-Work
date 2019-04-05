from flask import Flask, render_template, request, redirect, flash, session
from mysqlconnection import connectToMySQL

app = Flask(__name__)
app.secret_key = 'Wow so secret'

@app.route('/')
def index():
    mysql = connectToMySQL('survey')
    languages = mysql.query_db("SELECT * FROM language")
    mysql = connectToMySQL('survey')
    location = mysql.query_db("SELECT * FROM location")

    return render_template('index.html', lang=languages, loc=location)

@app.route('/results')
def results():
    mysql = connectToMySQL('survey')
    user_data = mysql.query_db('select ninja.name, ninja.comment, max(ninja.id), language.lang, location.locale, sex.sex from ninja as ninja left join location on ninja.location_id = location.id left join language on ninja.language_id = language.id left join sex on ninja.sex_id = sex.id group by ninja.id;')

    return render_template('results.html', user_data = user_data)


@app.route('/submit', methods=['POST'])
def process():
    print('*'*50, request.form)
    if len(request.form['username']) < 1:
        flash('Please enter a username!')
    if len(request.form['location']) < 1:
        flash('Please select a location!')   
    if len(request.form['language']) < 1:
        flash('Please select a language!')
    # if len(request.form['sex-radio']) < 1:
        # flash('Please select an option for sex!')
    if len(request.form['comment']) > 120:
        flash('Yer comment is too long!')   
   
    if not '_flashes' in session.keys():
        print('here')
        mysql = connectToMySQL('survey')

        query = "INSERT INTO ninjas (language_id, location_id, sex_id, name, comment, create_at, updated_at) VALUES((SELECT id FROM language where lang = '%(lang)s'), (SELECT id FROM location where locale = '%(loc)s'), (SELECT id from sex where sex = '%(sex)s'), %(nm)s, %(comm)s, now(), now());"
        
        data = {
            'nm': request.form['username'],
            'loc': request.form['location'],
            'lang': request.form['language'],
            'sex': request.form['sex-radio'],
            'comm': request.form['comment']
        }

        mysql = connectToMySQL('survey')
        new_user = mysql.query_db(query, data)
        flash('Submission successful!')

    return redirect('/results')

if __name__ == "__main__":
    app.run(debug=True)
