from flask import Blueprint, render_template


def home():
    return render_template("home.html")

def resume():
    return render_template("resume.html")

bp = Blueprint("webui", __name__, template_folder="templates")
bp.add_url_rule("/", view_func=home)
bp.add_url_rule("/resume", view_func=resume)


def init_app(app):
    app.register_blueprint(bp)
