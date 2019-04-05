from flask import Flask, render_template, request, redirect
from mysqlconnection import connectToMySQL

app = Flask(__name__)

@app.route('/users')
def users():
    mysql = connectToMySQL('users')
    users = mysql.query_db("SELECT id, CONCAT(first_name, ' ', last_name) as full_name, email, description, created_at, updated_at from users;")
    print(users)
    return render_template('index.html', all_users=users)

@app.route('/users/new')
def addUser():
    return render_template('add_user.html')

@app.route('/users/create', methods=['POST'])
def createUser():
    mysql = connectToMySQL('users')
    query = "INSERT INTO users(first_name, last_name, email, description, created_at, updated_at) VALUES(%(fn)s, %(ln)s, %(em)s, %(desc)s, NOW(), NOW());"
    
    data = {
        'fn': request.form['first_name'],
        'ln': request.form['last_name'],
        'em': request.form['email'],
        'desc': request.form['description']
    }

    new_user_id = mysql.query_db(query, data)
    return redirect('/users/' + str(new_user_id))

@app.route('/users/<x>')
def displayUser(x):
    print(x)
    mysql = connectToMySQL('users')
    user = mysql.query_db('SELECT id, CONCAT(first_name, " ", last_name) as full_name, email, description, created_at, updated_at FROM users WHERE id = ' + str(x) + ';')
    print('*'*30, user)
    return render_template('disp_user.html', user_data=user)

@app.route('/users/<x>/edit')  
def editUser(x):
    mysql = connectToMySQL('users')
    user = mysql.query_db('SELECT * FROM users WHERE id = ' + str(x) + ';')
    print('*'*30, user)
    return render_template('edit_user.html', user_data=user)

@app.route('/users/<x>/update', methods=['POST'])
def updateUser(x):
    mysql = connectToMySQL('users')
    query = "UPDATE users SET first_name = %(fn)s, last_name = %(ln)s, email = %(em)s, description = %(desc)s, updated_at = NOW() WHERE id = " + str(x) + ';'    
    
    data = {
        'fn': request.form['first_name'],
        'ln': request.form['last_name'],
        'em': request.form['email'],
        'desc': request.form['description']
    }

    user_id = mysql.query_db(query, data)
    return redirect('/users/' + x)

@app.route('/users/<x>/destroy')
def delUser(x):
    mysql = connectToMySQL('users')
    user = mysql.query_db('DELETE FROM users WHERE id = ' + x)

    return redirect('/users')

if __name__ == '__main__':
    app.run(debug=True)