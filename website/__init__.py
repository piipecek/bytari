from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()

def create_app() -> Flask:
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "abcd"
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///database.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
    app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_recycle' : 280}

    db.init_app(app)

    from .views.guest_views import guest_views
    from .views.auth_views import auth_views
    from .views.user_views import user_views


    app.register_blueprint(guest_views, url_prefix="/")
    app.register_blueprint(auth_views, url_prefix="/auth")
    app.register_blueprint(user_views, url_prefix = "/")

    from .models.user import User
 
    with app.app_context():
        db.create_all()

    login_manager.login_view = "auth_views.login"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))  # get rovou kouka na primary key, nemusim delat filter_by(id=id)

    @app.errorhandler(404)
    def not_found(e):
        return render_template("not_found.html"), 404

    @app.errorhandler(401)
    def not_authorised(e):
        return render_template("not_authorised.html"), 401

    return app