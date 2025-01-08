from flask import Blueprint, render_template, request, redirect, url_for, flash
from website.models.user import User
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_required, login_user, logout_user, current_user
from website import db

auth_views = Blueprint("auth_views",__name__, template_folder="auth")

@auth_views.route("/login", methods=["GET","POST"])
def login():
	if current_user.is_authenticated:
		return redirect(url_for("user_views.dashboard"))
	if request.method == "GET":
		return render_template("login.html")
	else:
		email = request.form.get("email")
		password = request.form.get("password")
		if len(email) > 100:
			flash("Zadaný e-mail byl určitě přiliš dlouhý.", category="error")
			return redirect(url_for("auth_views.login"))
		if len(password) > 300:    
			flash("Zadané heslo bylo určitě příliš dlouhé.", category="error")
			return redirect(url_for("auth_views.login"))
		user = User.get_by_email(email=email)
		if user and check_password_hash(user.password, password):
			login_user(user)
			flash("úspěšné přihlášení", category="success")
			return redirect(url_for("user_views.dashboard"))
		else:
			flash("E-mail nebo heslo byly špatně", category="error")
			return redirect(url_for("auth_views.login"))

@auth_views.route("/register", methods=["GET","POST"])
def register():
	if current_user.is_authenticated:
		return redirect(url_for("user_views.dashboard"))
	if request.method == "GET":
		return render_template("register.html")
	else:
		email = request.form.get("email")
		password = request.form.get("password")

		user = User.get_by_email(email=email)
		if user:
			flash("Tento email je už zaregistrovaný. Použij prosím jiný", category="error")
			return redirect(url_for("auth_views.register"))
		else:
			new_user = User(email=email, password=generate_password_hash(password, method="scrypt"))
			db.session.add(new_user)
			db.session.commit()
			flash("Úspěšná registrace.", category="success")
			return redirect(url_for("user_views.dashboard"))

@auth_views.route("/logout")
@login_required
def logout():
	logout_user()
	flash("Odhlášení proběhlo úspěšně.", category="info")
	return redirect(url_for("guest_views.home"))

