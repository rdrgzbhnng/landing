from flask import Blueprint, render_template, redirect


def home():
    return render_template("home.html")

def resume():
    return render_template("resume.html")

def book():
    return redirect("https://gitlab.com/rdrgzbhnng/docs/-/raw/master/rdrgzbhnng-book.pdf?inline=false")

def cv():
    return redirect("https://gitlab.com/rdrgzbhnng/docs/-/raw/master/rdrgzbhnng-cv.pdf?inline=false")


bp = Blueprint("webui", __name__, template_folder="templates")
bp.add_url_rule("/", view_func=home)
bp.add_url_rule("/resume", view_func=resume)
bp.add_url_rule("/book", view_func=book)
bp.add_url_rule("/cv", view_func=cv)

def init_app(app):
    app.register_blueprint(bp)
