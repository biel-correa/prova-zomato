from app import app
from flask import render_template
from database import restaurantes
from pages.restaurantes.RestauranteService import RestauranteService

@app.route('/restaurante/<int:id>', methods=['GET'])
def restaurante(id):
    restaurante = RestauranteService.getById(id)
    return render_template('detalhes.html', restaurante = restaurante)
