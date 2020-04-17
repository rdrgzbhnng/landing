from flask import Flask, render_template
from rdbh.extensions import configuration, appearance


app = Flask(__name__)

configuration.init_app(app)
appearance.init_app(app)


@app.route('/')
def index():
    return render_template("index.html")

if __name__ == '__main__':
    app.run()
