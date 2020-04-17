from flask import Flask, render_template
from rdbh.extensions import configuration
from flask_bootstrap import Bootstrap

app = Flask(__name__)

configuration.init_app(app)
Bootstrap(app)

@app.route('/')
def index():
    return render_template("index.html")

if __name__ == '__main__':
    app.run()
