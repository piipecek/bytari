from flask import Flask, render_template
import json
from pathlib import Path
volno_path = Path('volno.json')

def create_app() -> Flask:
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "abcd"
    
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