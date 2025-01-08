from flask import Blueprint, render_template, redirect, url_for
from flask_login import current_user


user_views = Blueprint("user_views",__name__)


@user_views.route("/dashboard")
def dashboard():
    if current_user.is_authenticated:
        return render_template("dashboard.html")