from flask import Flask, render_template
from dynaconf import FlaskDynaconf
from flask_bootstrap import Bootstrap

app = Flask(__name__)
FlaskDynaconf(app)
Bootstrap(app)

@app.route('/')
def index():
    return render_template("index.html")

if __name__ == '__main__':
    app.run()
