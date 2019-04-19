from config import app
from controller import index, register, login, success, logout

app.add_url_rule('/', view_func= index)
app.add_url_rule('/register', view_func= register, methods=["POST"])
app.add_url_rule('/login', view_func= login, methods=["POST"])
app.add_url_rule('/success', view_func= success)
app.add_url_rule('/logout', view_func= logout)