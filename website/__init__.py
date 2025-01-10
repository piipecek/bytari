from flask import Flask, render_template

def create_app() -> Flask:
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "abcd"


    from .views import views
    from .api import api

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(api, url_prefix="/")

    @app.errorhandler(404)
    def not_found(e):
        return render_template("not_found.html"), 404

    return app