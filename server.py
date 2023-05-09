from flask import Flask, render_template, redirect, request

from users import User

app = Flask(__name__)

@app.route('/')
def index():
    return redirect('/users')


@app.route('/users')
def users():
    return render_template('users.html', users = User.get_all())

@app.route('/users/new')
def show_users():
    return render_template('new_user.html')

@app.route('/home')
def home():
    return redirect('/users')

@app.route('/new_user')
def new_user():
    return redirect('/users/new')

if __name__ == "__main__":
    app.run(debug=True)