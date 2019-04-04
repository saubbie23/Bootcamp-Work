from flask import Flask, render_template, request, redirect
from mysqlconnection import connectToMySQL

app = Flask(__name__)
@app.route('/')
def index():
    mysql = connectToMySQL('pets')
    pets = mysql.query_db('select * from pets;')
    print(pets)
    return render_template('index.html', all_pets = pets)

@app.route('/create_pet', methods=['POST'])
def create_pet():
    mysql = connectToMySQL('pets')
    query = "INSERT INTO pets(name, type, created_at, updated_at) VALUES(%(nm)s, %(typ)s, NOW(), NOW());"
    
    print(query)
    data = {
        'nm': request.form['name'],
        'typ': request.form['type']
    }
    new_pet_id = mysql.query_db(query, data)
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)