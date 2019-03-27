from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def result():
    print('*'*50)
    print(request.form)
    return render_template('results.html', user_data=request.form)

if __name__ == "__main__":
    app.run(debug=True)


# ImmutableMultiDict([('username', 'dfaf'), ('location', ''), ('language', ''), ('sex-radio', 'option1'), ('comment', 'fsfdgs'), ('email-check', 'on')])