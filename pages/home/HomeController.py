from app import app
from flask import render_template, redirect
from database import restaurantes

@app.route('/', methods=['GET'])
def home():
    return render_template('home.html', restaurantes = restaurantes)

@app.route('/home', methods=['GET'])
def home_redirect():
    return redirect('/')