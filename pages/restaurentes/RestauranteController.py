from app import app
from flask import render_template, redirect
from database import restaurantes

#get restaurant by id
@app.route('/restaurante/<int:id>', methods=['GET'])
def restaurante(id):
    return render_template('home.html', restaurantes = restaurantes)
