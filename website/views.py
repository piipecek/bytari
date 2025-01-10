from flask import Blueprint, render_template, request, redirect, url_for
from .pozvanky_handling import vynulovat_by_id, toggle_zamknuti_by_id


views = Blueprint("views",__name__)


@views.route("/", methods=["GET", "POST"])
def home():
    if request.method == "GET":
        return render_template("home.html")
    else:
        return request.form.to_dict()

@views.route("/admin", methods=["GET", "POST"])
def admin():
    if request.method == "GET":
        return render_template("admin.html")
    
    if request.method == "POST":
        if id := request.form.get("vynulovat"):
            vynulovat_by_id(int(id))
        elif id := request.form.get("toggle"):
            toggle_zamknuti_by_id(int(id))
        
    return redirect(url_for("views.admin"))
        