from flask import Flask, render_template

app = Flask(__name__)

@app.route('/play')
def play():
    return render_template('index.html', times=3, col='blue')

@app.route('/play/<num>')
def level2(num):
    print(num)
    return render_template('index.html', times=int(num), col='blue')

@app.route('/play/<num>/<color>')
def level3(num, color):
    return render_template('index.html', times=int(num),col=color)    

if __name__ == "__main__":
    app.run(debug=True) b 