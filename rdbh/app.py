from flask import Flask
from rdbh.extensions import configuration
from rdbh.blueprints.webui import views


app = Flask(__name__)

configuration.init_app(app)
views.init_app(app)
