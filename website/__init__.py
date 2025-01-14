from flask import Flask, render_template
from flask_mail import Mail
import json
from pathlib import Path
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path=Path.cwd() / ".env")
mail = Mail()

def create_app() -> Flask:
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "abcd"
    app.config["MAIL_SERVER"] = os.environ.get("MAIL_SERVER")
    app.config["MAIL_PORT"] = os.environ.get("MAIL_PORT")
    app.config["MAIL_USE_SSL"] = True
    app.config["MAIL_USERNAME"] = os.environ.get("MAIL_USERNAME")
    app.config["MAIL_PASSWORD"] = os.environ.get("MAIL_PASSWORD")
    
    mail.init_app(app)
    
    volno_path = Path('volno.json')
    if not volno_path.exists():
        with volno_path.open("w") as f:
            json.dump([], f)


    from .views import views
    from .api import api

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(api, url_prefix="/")

    @app.errorhandler(404)
    def not_found(e):
        return render_template("not_found.html"), 404

    return app