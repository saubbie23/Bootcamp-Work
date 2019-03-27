from flask import Flask, render_template, redirect, session, request

app = Flask(__name__)
app.secret_key = 'much secret'

def countVisit():
    if 'visits' in session:
        session['visits'] += 1
        session['counter'] += 1
    else:
        session['visits'] = 1
        session['counter'] = 1          

@app.route('/')
def index():
    countVisit()
    if 'add_var' in session:
        session['counter'] += session['increment']
    return render_template('index.html')

@app.route('/destroy_session')
def destroy():
    session.clear()
    return redirect('/')

@app.route('/add_var', methods=['POST', 'GET'])
def add_two():
    try:
        increment = int(request.form['increment'])

    except:
        increment = 2
                
    if 'add_var' in session:
        session.pop('add_var')
        session.pop('increment')

    session['add_var'] = True
    session['increment'] = increment - 1     
    return redirect('/')

@app.route('/add_var', methods=['POST'])   
def add_var():
    print(request.form)
    return redirect('/') 

@app.route('/clear')
def clear():
    session.clear()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)