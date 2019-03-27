from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World!"

@app.route('/dojo')
def dojo():
    return "Dojo!"    

@app.route('/say/<name>')
def hello_name(name):
    try:
        int(name)
        return "Invalid name!"
    except:
         return f"Hello {name}!"   

@app.route('/repeat/<num>/<word>')
def repeat(num,word):
    try:
        int(num)       
        return word*int(num)
    except:
        return "Invalid Inputs!" 

@app.route('/<any>')
def error_handle(any):
    return "Sorry, no response! Try again!"

if __name__ == "__main__":
    app.run(debug=True)    