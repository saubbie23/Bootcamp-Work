from flask import Flask, render_template, redirect, request, session
from random import randint

app = Flask(__name__)
app.secret_key = 'Big Ron'

@app.route('/')
def index():
    rand_num = randint(1,100)

    if 'rand_num' not in session:
        session['rand_num'] = rand_num
    if 'num_guess' not in session:    
        session['num_guess'] = 0
    print(session)
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess():
    guess = int(request.form['user_guess'])

    if guess > session['rand_num']:
        session['response']  = 'Too high, nerd!'
        session['num_guess'] += 1
    elif guess < session['rand_num']:
        session['response']  = 'Wow, so low, loser!'
        session['num_guess'] += 1
    else:
        session['response'] = 'Nailed it. So lucky'
        session['num_guess'] +=1
    if session['num_guess'] == 5:
        session['lose'] = True     
    return redirect('/') 

@app.route('/reset')
def reset():
    session.pop('response')
    session.pop('num_guess')
    session.pop('rand_num')
    return redirect('/')

@app.route('/winner', methods=['POST'])
def winner():
    print(request.form)
    if 'leader_names' not in session:
        session['leader_names'] =[request.form['winner']]
        session['leader_guess'] = [session['num_guess']]
    else:
        leader_names = session['leader_names']
        leader_names.append(request.form['winner'])
        session['leader_names'] = leader_names

        num_guesses = session['leader_guess']
        num_guesses.append(session['num_guess'])
        session['leader_guess'] = num_guesses

    print('*'*20,session)        
    return render_template('winner.html')   

if __name__ == '__main__':
    app.run(debug=True)