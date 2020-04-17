from flask import Flask
from rdbh.extensions import configuration, appearance
from rdbh.blueprints import routes


app = Flask(__name__)

configuration.init_app(app)
appearance.init_app(app)
routes.init_app(app)
