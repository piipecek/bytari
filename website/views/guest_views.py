from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import current_user


guest_views = Blueprint("guest_views",__name__)


@guest_views.route("/")
def home():
    return render_template("home.html", current_user=current_user)