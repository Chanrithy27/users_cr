from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.user import User


@app.route('/')
def index():
    return redirect('/users')


@app.route('/users')
def users():
    return render_template('users.html', users = User.get_all())

@app.route('/users/new')
def show_users():
    return render_template('new_user.html')

@app.route('/create_user', methods = ['POST'])
def create():
    User.save(request.form)
    return redirect('/users')

@app.route('/home')
def home():
    return redirect('/users')

@app.route('/new_user')
def new_user():
    return redirect('/users/new')