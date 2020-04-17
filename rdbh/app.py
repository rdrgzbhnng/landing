from flask import Flask
from rdbh.extensions import configuration, appearance, views


app = Flask(__name__)

configuration.init_app(app)
appearance.init_app(app)
views.init_app(app)
