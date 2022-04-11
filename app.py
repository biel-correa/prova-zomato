from flask import Flask

app = Flask(__name__)

from pages.home import HomeController
from pages.restaurentes import RestauranteController

if __name__ == '__main__':
    app.run()